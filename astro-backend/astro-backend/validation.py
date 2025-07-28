import re
from datetime import datetime
from typing import Optional

def validate_date(date_str: str) -> bool:
    """Validate date format YYYY-MM-DD"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_time(time_str: str) -> bool:
    """Validate time format HH:MM"""
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def validate_coordinates(lat: float, lon: float) -> bool:
    """Validate latitude and longitude"""
    return -90 <= lat <= 90 and -180 <= lon <= 180

def validate_tz_offset(tz_offset: float) -> bool:
    """Validate timezone offset"""
    return -12 <= tz_offset <= 14

def validate_gender(gender: str) -> bool:
    """Validate gender parameter"""
    return gender.lower() in ["male", "female", "other"]

def sanitize_string(input_str: str) -> str:
    """Sanitize string input to prevent injection attacks"""
    # Remove any potentially dangerous characters
    return re.sub(r'[<>"\']', '', input_str.strip())

def validate_birth_data(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5) -> tuple[bool, Optional[str]]:
    """Validate all birth data inputs"""
    if not validate_date(dob):
        return False, "Invalid date format. Use YYYY-MM-DD"
    
    if not validate_time(tob):
        return False, "Invalid time format. Use HH:MM"
    
    if not validate_coordinates(lat, lon):
        return False, "Invalid coordinates. Latitude must be between -90 and 90, longitude between -180 and 180"
    
    if not validate_tz_offset(tz_offset):
        return False, "Invalid timezone offset. Must be between -12 and 14"
    
    return True, None 