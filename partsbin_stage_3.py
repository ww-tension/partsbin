# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: PartsBin
def validate_required(value, name):
    if not value:
        raise ValueError(f"{name} is required")
    return value

def validate_identifier(value, name):
    if not value or not value.strip():
        raise ValueError(f"{name} must be a non-empty identifier")
    return value.strip().lower()

def validate_short_text(value, name, max_length=50):
    if not value:
        raise ValueError(f"{name} is required")
    if len(value) > max_length:
        raise ValueError(f"{name} exceeds {max_length} characters")
    return value.strip()

def validate_positive_integer(value, name):
    try:
        iv = int(value)
        if iv <= 0:
            raise ValueError(f"{name} must be a positive integer")
        return iv
    except (TypeError, ValueError):
        raise ValueError(f"{name} must be a valid positive integer")
