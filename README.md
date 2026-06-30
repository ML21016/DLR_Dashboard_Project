# Journal Bearing Predictive Maintenance Dashboard

An end-to-end Machine Learning web application designed to monitor journal bearing health conditions and predict structural degradation in real-time. This system transitions physical tribological research concepts into an automated software pipeline, preventing catastrophic component failures through early-stage fault classification.

---

## Key Features
* **Industrial Data Ingestion:** Automated pipeline parsing raw high-frequency multi-channel `.mat` data streams.
* **Feature Engineering Pipeline:** Maps raw sensor metrics over time into statistical signatures including Mean, Standard Deviation, Minimum, and Maximum.
* **Machine Learning Diagnostics:** Employs a trained Random Forest Classifier to identify critical transitions through boundary, mixed, and hydrodynamic friction regimes.
* **Interactive Operator UI:** A streamlined, functional frontend dashboard for on-the-fly file uploads, feature calculation, and maintenance hazard alerting.

---

## Technical Stack
* **Language:** Python
* **Frontend Dashboard:** Streamlit
* **Machine Learning:** Scikit-Learn
* **Data Processing:** NumPy, SciPy, Pandas
* **Version Control:** Git / GitHub

---

## Sensor Array Tracked
The model evaluates synchronous data across four vital system channels:
1. **Kontakt_V:** Contact Voltage (crucial for mapping lubrication film thickness and friction transitions)
2. **Force:** Structural loads on the journal bearing assembly
3. **Torque:** Rotational resistance changes indicative of early component wear
4. **Rotation_speed:** Real-time operating velocity matrix

---

## How to Run the App Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/ML21016/predictive-maintenance-dashboard.git](https://github.com/ML21016/predictive-maintenance-dashboard.git)
