# backend/utils.py

def encode_gender(value):
    mapping = {"Male": 1, "Female": 0, "Non-binary": 2}
    return mapping.get(value, 1)

def encode_status(value):
    mapping = {"Student": 1, "Working": 0, "Both": 2}
    return mapping.get(value, 1)