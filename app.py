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
            # 2. Load the .mat file safely
            mat = scipy.io.loadmat(file_path)
            
            # Extract key dynamically
            key = [k for k in mat.keys() if not k.startswith('__')][0]
            data = mat[key]
            
            # Fix column orientation if it's transposed
            if data.shape[1] == 1 and data.shape[0] > 1:
                # If it loaded as a single column or weird 1D shape, fall back gracefully
                v_win = data.flatten()
                f_win = data.flatten()
                t_win = data.flatten()
            elif data.shape[0] < data.shape[1]:
                # If rows and columns are swapped
                v_win = data[0, :]
                f_win = data[1, :] if data.shape[0] > 1 else data[0, :]
                t_win = data[2, :] if data.shape[0] > 2 else data[0, :]
            else:
                # Standard expected shape
                v_win = data[:, 0]
                f_win = data[:, 1]
                t_win = data[:, 2]
            
            # 3. Engineering the exact features my model expects
            features = np.array([[
                np.mean(v_win),
                np.min(v_win),
                np.std(v_win),
                np.mean(f_win),
                np.max(f_win),
                np.mean(t_win),
                np.max(t_win)
            ]])
            
            # 4. Make prediction
            prediction = model.predict(features)[0]
            
            # 5. Display the result beautifully
            st.markdown("---")
            if prediction == 1:
                st.error("🚨 DIAGNOSTIC STATUS: FAILING (Urgent Maintenance Required)")
            else:
                st.success("✅ DIAGNOSTIC STATUS: HEALTHY (Operational)")
                
        except Exception as e:
            st.error(f"Error analyzing data structure: {e}")
    else:
        st.warning("Please provide a valid file path first.")