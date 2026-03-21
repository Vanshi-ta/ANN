# backend/iks_engine.py

import random

# -------------------------------
# IKS Knowledge Base
# -------------------------------

IKS_LIBRARY = {
    "Low": [
        {"name": "Light Yoga", "type": "physical"},
        {"name": "Mindful Breathing", "type": "breathing"},
        {"name": "Stretching Routine", "type": "physical"}
    ],
    "Medium": [
        {"name": "Pranayama", "type": "breathing"},
        {"name": "Surya Namaskar", "type": "physical"},
        {"name": "Meditation", "type": "mental"}
    ],
    "High": [
        {"name": "Yoga Nidra", "type": "deep_rest"},
        {"name": "Anulom Vilom", "type": "breathing"},
        {"name": "Guided Meditation", "type": "mental"}
    ]
}

# -------------------------------
# Duration Logic
# -------------------------------

def get_duration(free_time):
    if free_time < 10:
        return "5–7 minutes"
    elif free_time < 20:
        return "10–15 minutes"
    else:
        return "20–30 minutes"

# -------------------------------
# Intensity Logic
# -------------------------------

def get_intensity(age, fitness):
    if age > 35 or fitness == "low":
        return "gentle"
    elif fitness == "high":
        return "intense"
    else:
        return "moderate"

# -------------------------------
# Preference Filter
# -------------------------------

def filter_by_preference(options, preference):
    if preference is None:
        return options

    filtered = [opt for opt in options if opt["type"] == preference]

    return filtered if filtered else options


# -------------------------------
# MAIN FUNCTION
# -------------------------------

def generate_iks_plan(burnout, age, free_time, fitness, preference=None):

    # get base options
    options = IKS_LIBRARY[burnout]

    # apply preference filter
    options = filter_by_preference(options, preference)

    # random selection (non-static)
    suggestion = random.choice(options)

    name = suggestion["name"]

    # duration
    duration = get_duration(free_time)

    # intensity
    intensity = get_intensity(age, fitness)

    # explanation (VERY IMPORTANT)
    reason = f"""
Based on your burnout level ({burnout}), age ({age}), and available time ({free_time} minutes),
a {intensity} session of {name} for {duration} is recommended.

Since your current lifestyle indicates moderate mental load, this practice will help:
• reduce stress levels
• improve focus and clarity
• stabilize emotional balance
"""

    # structured response
    return {
        "title": f"{burnout} Burnout Recovery Plan",
        "activity": name,
        "duration": duration,
        "intensity": intensity,
        "reason": reason.strip()
    }