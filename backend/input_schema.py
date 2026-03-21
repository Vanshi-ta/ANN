# backend/input_schema.py

def split_user_input(user_data):
    """
    Splits user input into:
    1. ANN model input
    2. IKS recommendation input
    """

    # ANN input (ONLY what model expects)
    ann_input = [
        user_data["Age"],
        user_data["Gender"],
        user_data["Student_Working_Status"],
        user_data["Daily_Social_Media_Hours"],
        user_data["Screen_Time_Hours"],
        user_data["Night_Scrolling_Frequency"],
        user_data["Online_Gaming_Hours"],
        user_data["Exercise_Frequency_per_Week"],
        user_data["Daily_Sleep_Hours"],
        user_data["Caffeine_Intake_Cups"],
        user_data["Study_Work_Hours_per_Day"],
        user_data["Overthinking_Score"],
        user_data["Anxiety_Score"],
        user_data["Mood_Stability_Score"],
        user_data["Social_Comparison_Index"],
        user_data["Sleep_Quality_Score"],
        user_data["Motivation_Level"],
        user_data["Emotional_Fatigue_Score"]
    ]

    # IKS-specific inputs (NEW)
    iks_input = {
        "age": user_data["Age"],
        "free_time": user_data["free_time_minutes"],
        "fitness_level": user_data["fitness_level"],
        "preference": user_data.get("preference", None)
    }

    return ann_input, iks_input