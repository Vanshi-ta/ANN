# backend/test_model_behavior.py

from predictor import predict_burnout

# -------------------------------
# TEST CASES
# -------------------------------

test_cases = [

    # ============================
    # LOW BURNOUT (Healthy lifestyle)
    # ============================
    {
        "name": "LOW_1 (Very Healthy)",
        "data": [22, 1, 1, 2, 3, 1, 0, 5, 8, 1, 5, 2, 2, 8, 2, 8, 8, 2]
    },
    {
        "name": "LOW_2 (Balanced life)",
        "data": [25, 0, 0, 3, 4, 2, 1, 4, 7, 1, 6, 3, 3, 7, 3, 7, 7, 3]
    },

    # ============================
    # MEDIUM BURNOUT
    # ============================
    {
        "name": "MEDIUM_1 (Moderate stress)",
        "data": [23, 1, 1, 5, 7, 5, 2, 2, 6, 2, 8, 6, 6, 5, 6, 5, 5, 6]
    },
    {
        "name": "MEDIUM_2 (Work heavy)",
        "data": [28, 1, 0, 6, 8, 6, 3, 1, 6, 3, 9, 6, 6, 5, 6, 5, 4, 7]
    },

    # ============================
    # HIGH BURNOUT (Unhealthy)
    # ============================
    {
        "name": "HIGH_1 (Severe burnout)",
        "data": [21, 1, 1, 10, 12, 9, 5, 0, 4, 4, 12, 9, 9, 3, 8, 3, 3, 9]
    },
    {
        "name": "HIGH_2 (Extreme stress)",
        "data": [26, 0, 0, 9, 11, 8, 4, 0, 5, 5, 11, 8, 9, 2, 9, 2, 2, 10]
    },

    # ============================
    # EDGE CASES
    # ============================
    {
        "name": "EDGE_LOW_SLEEP",
        "data": [24, 1, 1, 4, 6, 3, 1, 3, 3, 2, 7, 5, 6, 5, 5, 4, 4, 6]
    },
    {
        "name": "EDGE_HIGH_EXERCISE",
        "data": [24, 1, 1, 6, 7, 4, 2, 7, 7, 1, 6, 4, 4, 7, 4, 7, 7, 3]
    }
]


# -------------------------------
# RUN TESTS
# -------------------------------

print("\n===== MODEL BEHAVIOR TEST =====\n")

for case in test_cases:
    burnout, confidence = predict_burnout(case["data"])

    print(f"Test Case: {case['name']}")
    print(f"Prediction: {burnout}")
    print(f"Confidence: {round(confidence * 100, 2)}%")
    print("-" * 40)


# -------------------------------
# MULTIPLE RUN CHECK (IMPORTANT)
# -------------------------------

print("\n===== CONSISTENCY TEST =====\n")

sample = test_cases[4]["data"]  # HIGH case

for i in range(5):
    burnout, confidence = predict_burnout(sample)
    print(f"Run {i+1}: {burnout} ({round(confidence*100,2)}%)")