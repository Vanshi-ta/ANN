# backend/test_full.py

from input_schema import split_user_input
from predictor import predict_burnout
from iks_engine import generate_iks_plan

# full user input
user_data = {
    "Age": 24,
    "Gender": 1,
    "Student_Working_Status": 1,
    "Daily_Social_Media_Hours": 5,
    "Screen_Time_Hours": 8,
    "Night_Scrolling_Frequency": 3,
    "Online_Gaming_Hours": 2,
    "Exercise_Frequency_per_Week": 2,
    "Daily_Sleep_Hours": 5.5,
    "Caffeine_Intake_Cups": 3,
    "Study_Work_Hours_per_Day": 8,
    "Overthinking_Score": 7,
    "Anxiety_Score": 7,
    "Mood_Stability_Score": 4,
    "Social_Comparison_Index": 6,
    "Sleep_Quality_Score": 4,
    "Motivation_Level": 4,
    "Emotional_Fatigue_Score": 8,

    # NEW INPUTS
    "free_time_minutes": 12,
    "fitness_level": "low",
    "preference": "breathing"
}

# split inputs
ann_input, iks_input = split_user_input(user_data)

# predict burnout
burnout, confidence = predict_burnout(ann_input)


# generate recommendation
plan = generate_iks_plan(
    burnout=burnout,
    age=iks_input["age"],
    free_time=iks_input["free_time"],
    fitness=iks_input["fitness_level"],
    preference=iks_input["preference"]
)

# output
print("\nBurnout Level:", burnout)
print("Confidence:", round(confidence * 100, 2), "%")
print("\nRecommended Plan:")
print(plan)