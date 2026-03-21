# backend/test_input.py

from input_schema import split_user_input
from predictor import predict_burnout

# sample user input (WITH new fields)
user_data = {
    "Age": 22,
    "Gender": 1,
    "Student_Working_Status": 1,
    "Daily_Social_Media_Hours": 5,
    "Screen_Time_Hours": 7,
    "Night_Scrolling_Frequency": 3,
    "Online_Gaming_Hours": 2,
    "Exercise_Frequency_per_Week": 3,
    "Daily_Sleep_Hours": 6,
    "Caffeine_Intake_Cups": 2,
    "Study_Work_Hours_per_Day": 7,
    "Overthinking_Score": 6,
    "Anxiety_Score": 7,
    "Mood_Stability_Score": 5,
    "Social_Comparison_Index": 6,
    "Sleep_Quality_Score": 5,
    "Motivation_Level": 5,
    "Emotional_Fatigue_Score": 7,

    # 🔥 NEW FIELDS (IKS)
    "free_time_minutes": 15,
    "fitness_level": "medium",
    "preference": "breathing"
}

# split input
ann_input, iks_input = split_user_input(user_data)

# prediction
burnout, confidence = predict_burnout(ann_input)

print("Burnout Level:", burnout)
print("Confidence:", round(confidence * 100, 2), "%")
print("IKS Input:", iks_input)