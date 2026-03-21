# backend/predictor.py

import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


# load model
model = load_model("../model/mental_health_ann_model.keras")
scaler = joblib.load("../model/scaler.pkl")

# feature order MUST match training
feature_names = [
    "Age",
    "Gender",
    "Student_Working_Status",
    "Daily_Social_Media_Hours",
    "Screen_Time_Hours",
    "Night_Scrolling_Frequency",
    "Online_Gaming_Hours",
    "Exercise_Frequency_per_Week",
    "Daily_Sleep_Hours",
    "Caffeine_Intake_Cups",
    "Study_Work_Hours_per_Day",
    "Overthinking_Score",
    "Anxiety_Score",
    "Mood_Stability_Score",
    "Social_Comparison_Index",
    "Sleep_Quality_Score",
    "Motivation_Level",
    "Emotional_Fatigue_Score"
]

burnout_labels = {
    0: "Low",
    1: "Medium",
    2: "High"
}

def predict_burnout(ann_input):

    df = pd.DataFrame([ann_input], columns=feature_names)

    scaled = scaler.transform(df)

    prediction = model.predict(scaled)

    predicted_class = np.argmax(prediction)
    confidence = float(np.max(prediction))

    return burnout_labels[predicted_class], confidence