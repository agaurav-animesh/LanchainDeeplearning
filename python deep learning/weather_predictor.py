import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.title(" Weather Predictor using Random Forest")


np.random.seed(42)
data_size = 500
df = pd.DataFrame({
    "temperature": np.random.uniform(10, 40, data_size),
    "humidity": np.random.uniform(30, 100, data_size),
    "wind_speed": np.random.uniform(0, 20, data_size),
    "pressure": np.random.uniform(950, 1050, data_size),
})


df["rain"] = np.where(
    (df["humidity"] > 70) & (df["temperature"] < 25), 1, 0
)

# Split data
X = df[["temperature", "humidity", "wind_speed", "pressure"]]
y = df["rain"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

st.write(f" Model trained with accuracy: **{acc:.2f}**")


st.sidebar.header("Enter current weather conditions:")
temp = st.sidebar.slider("Temperature (°C)", 0.0, 45.0, 25.0)
humidity = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 60.0)
wind = st.sidebar.slider("Wind Speed (km/h)", 0.0, 30.0, 10.0)
pressure = st.sidebar.slider("Pressure (hPa)", 900.0, 1100.0, 1010.0)


input_data = np.array([[temp, humidity, wind, pressure]])
prediction = model.predict(input_data)[0]

if prediction == 1:
    st.success(" It’s likely to rain!")
else:
    st.info(" No rain expected.")

st.subheader("Sample Weather Data")
st.dataframe(df.head())
