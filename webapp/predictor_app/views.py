from django.shortcuts import render

import sys
import os

# connect backend folder
sys.path.append(os.path.abspath("../backend"))

from predictor import predict_burnout
from input_schema import split_user_input
from iks_engine import generate_iks_plan


def home(request):
    return render(request, "form.html")


def safe_float(value, default):
    try:
        return float(value)
    except:
        return default


def safe_int(value, default):
    try:
        return int(value)
    except:
        return default
    

def predict(request):
    if request.method == "POST":

        # collect inputs
        user_data = {
            "Age": safe_float(request.POST.get("age"), 22),

            "Gender": safe_int(request.POST.get("gender"), 1),
            "Student_Working_Status": safe_int(request.POST.get("status"), 1),

            "Daily_Social_Media_Hours": safe_float(request.POST.get("social"), 5),
            "Screen_Time_Hours": safe_float(request.POST.get("screen"), 6),
            "Night_Scrolling_Frequency": safe_float(request.POST.get("scroll"), 2),
            "Online_Gaming_Hours": safe_float(request.POST.get("gaming"), 1),

            "Exercise_Frequency_per_Week": safe_float(request.POST.get("exercise"), 3),
            "Daily_Sleep_Hours": safe_float(request.POST.get("sleep"), 7),
            "Caffeine_Intake_Cups": safe_float(request.POST.get("caffeine"), 1),
            "Study_Work_Hours_per_Day": safe_float(request.POST.get("study"), 6),

            "Overthinking_Score": safe_float(request.POST.get("overthinking"), 5),
            "Anxiety_Score": safe_float(request.POST.get("anxiety"), 5),
            "Mood_Stability_Score": safe_float(request.POST.get("mood"), 5),
            "Social_Comparison_Index": safe_float(request.POST.get("comparison"), 5),
            "Sleep_Quality_Score": safe_float(request.POST.get("sleep_quality"), 5),
            "Motivation_Level": safe_float(request.POST.get("motivation"), 5),
            "Emotional_Fatigue_Score": safe_float(request.POST.get("fatigue"), 5),

            "free_time_minutes": safe_float(request.POST.get("time"), 10),

            "fitness_level": request.POST.get("fitness", "medium"),
            "preference": request.POST.get("preference") or None
        }

        if user_data["Gender"] == -1:
            user_data["Gender"] = 1  # default

        if user_data["Student_Working_Status"] == -1:
            user_data["Student_Working_Status"] = 1

        if user_data["fitness_level"] == "unknown":
            user_data["fitness_level"] = "medium"
            
        # split inputs
        ann_input, iks_input = split_user_input(user_data)

        # prediction
        burnout, confidence = predict_burnout(ann_input)

        # recommendation
        plan = generate_iks_plan(
            burnout=burnout,
            age=iks_input["age"],
            free_time=iks_input["free_time"],
            fitness=iks_input["fitness_level"],
            preference=iks_input["preference"]
        )

        return render(request, "result.html", {
            "burnout": burnout,
            "confidence": round(confidence * 100, 2),
            "plan": plan
        })