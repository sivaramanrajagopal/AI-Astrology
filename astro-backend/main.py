
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import os

# --- FastAPI App ---
app = FastAPI(
    title="Vedic Astrology API",
    description="A comprehensive Vedic astrology API with planetary calculations and AI-powered interpretations",
    version="1.0.0"
)

# --- CORS Settings ---
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,https://your-frontend-domain.vercel.app").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message":
        "Astrology API is running. Endpoints: /test, /predict, /career, /dasa, /yogas, /life_purpose, /dasa_bhukti, /spouse, /indu_dasa."
    }

@app.get("/test")
def test():
    """Simple test endpoint to verify server is running."""
    return {"status": "success", "message": "Server is running correctly!"}

@app.get("/predict")
def predict(dob: str,
            tob: str,
            lat: float,
            lon: float,
            tz_offset: float = 5.5):
    """Returns planetary positions and GPT-based predictions."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
        prompt = generate_gpt_prompt(data)
        interpretation = get_astrology_interpretation(prompt)
        return {"chart": data, "interpretation": interpretation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/career")
def career(dob: str,
           tob: str,
           lat: float,
           lon: float,
           tz_offset: float = 5.5):
    """Returns career analysis and recommendations."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from astrology import get_planet_positions
        from carear import analyze_career, generate_career_report
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
        career_analysis = analyze_career(data)
        career_report = generate_career_report(career_analysis)
        return {"chart": data, "career_analysis": career_analysis, "career_report": career_report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/dasa")
def dasa(dob: str,
         tob: str,
         lat: float,
         lon: float,
         tz_offset: float = 5.5):
    """Returns Dasa periods and predictions."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from astrology import get_planet_positions
        from dasa import generate_dasa_table
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
        dasa_table = generate_dasa_table(data)
        return {"chart": data, "dasa_table": dasa_table}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/yogas")
def yogas(dob: str,
          tob: str,
          lat: float,
          lon: float,
          tz_offset: float = 5.5):
    """Returns detected Yogas and their effects."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from astrology import get_planet_positions
        from allyogas import detect_yogas
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
        detected_yogas = detect_yogas(data)
        return {"chart": data, "yogas": detected_yogas}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/life_purpose")
def life_purpose(dob: str,
                tob: str,
                lat: float,
                lon: float,
                tz_offset: float = 5.5):
    """Returns life purpose analysis and guidance."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from astrology import get_planet_positions
        from life_purpose import analyze_life_purpose, generate_purpose_report
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
        purpose_analysis = analyze_life_purpose(data)
        purpose_report = generate_purpose_report(purpose_analysis)
        return {"chart": data, "purpose_analysis": purpose_analysis, "purpose_report": purpose_report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/dasa_bhukti")
def dasa_bhukti(dob: str,
                tob: str,
                lat: float,
                lon: float,
                tz_offset: float = 5.5):
    """Returns detailed Dasa-Bhukti periods and predictions."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from dasa_bhukti import get_planet_positions as get_dasa_positions, generate_dasa_table as generate_dasa_bhukti_table
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_dasa_positions(dob, tob, lat, lon, tz_offset)
        dasa_bhukti_table = generate_dasa_bhukti_table(data)
        return {"chart": data, "dasa_bhukti_table": dasa_bhukti_table}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/spouse")
def spouse(dob: str,
          tob: str,
          lat: float,
          lon: float,
          tz_offset: float = 5.5):
    """Returns spouse analysis and marriage predictions."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from spouse_analysis import get_planet_positions as get_spouse_positions, analyze_marriage, generate_report as spouse_report
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_spouse_positions(dob, tob, lat, lon, tz_offset)
        spouse_analysis = analyze_marriage(data)
        spouse_report_text = spouse_report(spouse_analysis)
        return {"chart": data, "spouse_analysis": spouse_analysis, "spouse_report": spouse_report_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/indu_dasa")
def indu_dasa(dob: str,
              tob: str,
              lat: float,
              lon: float,
              tz_offset: float = 5.5):
    """Returns Indu Dasa periods and predictions."""
    try:
        # Lazy import to avoid startup issues
        from validation import validate_birth_data
        from astrology import get_planet_positions
        from indu_dasa import get_indu_dasa
        
        is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
        
        data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
        indu_dasa_table = get_indu_dasa(data)
        return {"chart": data, "indu_dasa_table": indu_dasa_table}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
