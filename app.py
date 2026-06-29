import streamlit as st
import pickle
import numpy as np
import scipy.io

# 1. Load my saved model
with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# Set up interface headers
st.title("Machine Health Monitoring Dashboard")
st.write("Enter the absolute file path of a sensor .mat file to analyze its state.")

# User inputs file path
file_path = st.text_input("Sensor File Path:", "")

if st.button("Run Diagnostics"):
    if file_path:
        try:
            # 2. Load the .mat file exactly like the notebook
            mat_data = scipy.io.loadmat(file_path)
            
            # 3. Safely extract and flatten the exact 4 sensor arrays
            force = mat_data["Force"].flatten()
            kontakt_v = mat_data["Kontakt_V"].flatten()
            rotation_speed = mat_data["Rotation_speed"].flatten()
            torque = mat_data["Torque"].flatten()
            
            # 4. Engineer the precise features your model expects
            features = np.array([[
                kontakt_v.mean(),
                kontakt_v.min(),
                kontakt_v.std(),
                force.mean(),
                force.max(),
                torque.mean(),
                torque.max()
            ]])
            
            # 5. Make prediction
            prediction = model.predict(features)[0]
            
            # 6. Display the true result
            st.markdown("---")
            if prediction == 1:
                st.error("🚨 DIAGNOSTIC STATUS: FAILING (Urgent Maintenance Required)")
            else:
                st.success("✅ DIAGNOSTIC STATUS: HEALTHY (Operational)")
                
        except KeyError as ke:
            st.error(f"Missing expected sensor key in this file: {ke}")
        except Exception as e:
            st.error(f"Error running analysis: {e}")
    else:
        st.warning("Please provide a valid file path first.")