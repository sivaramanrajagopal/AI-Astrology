from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import datetime
import pyswisseph as swe
import os
from validation import validate_birth_data, sanitize_string

# --- Imports from other modules ---
from astrology import get_planet_positions, generate_gpt_prompt, get_astrology_interpretation
from carear import analyze_career, generate_career_report
from allyogas import detect_yogas
from dasa import generate_dasa_table
from life_purpose import analyze_life_purpose, generate_purpose_report, ask_gpt
from dasa_bhukti import get_planet_positions as get_dasa_positions, generate_dasa_table as generate_dasa_bhukti_table, ask_gpt_dasa_prediction
from spouse_analysis import get_planet_positions as get_spouse_positions, get_aspects as get_spouse_aspects, analyze_marriage, generate_report as spouse_report, ask_gpt_spouse
from indu_dasa import get_indu_dasa  # <--- NEW IMPORT

# --- FastAPI App ---
app = FastAPI(
    title="Vedic Astrology API",
    description="A comprehensive Vedic astrology API with planetary calculations and AI-powered interpretations",
    version="1.0.0"
)

# --- CORS Settings ---
# Get allowed origins from environment variable or use default
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,https://your-frontend-domain.vercel.app").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,  # Restrict to specific domains
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  # Restrict methods
    allow_headers=["*"],
)

# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {
        "message":
        "Astrology API is running. Endpoints: /predict, /career, /dasa, /yogas, /life_purpose, /dasa_bhukti, /spouse, /indu_dasa."
    }

# ---------------- PREDICT ----------------
@app.get("/predict")
def predict(dob: str,
            tob: str,
            lat: float,
            lon: float,
            tz_offset: float = 5.5):
    """Returns planetary positions and GPT-based predictions."""
    # Validate inputs
    is_valid, error_msg = validate_birth_data(dob, tob, lat, lon, tz_offset)
    if not is_valid:
        raise HTTPException(status_code=400, detail=error_msg)
    
    try:
        data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
        prompt = generate_gpt_prompt(data)
        interpretation = get_astrology_interpretation(prompt)
        return {"chart": data, "interpretation": interpretation}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

# ---------------- CAREER ----------------
@app.get("/career")
def career(dob: str,
           tob: str,
           lat: float,
           lon: float,
           tz_offset: float = 5.5,
           gender: str = "Male"):
    """Returns detailed career analysis."""
    data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon, tz_offset)
    analysis = analyze_career(data, asc_deg, cusps, gender)
    report = generate_career_report(analysis, asc_deg)
    return {"career_report": report}

# ---------------- DASA ----------------
@app.get("/dasa")
def dasa(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    """Returns Vimshottari Dasa timeline."""
    local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
    jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                    utc_dt.hour + utc_dt.minute / 60.0)
    swe.set_topo(lon, lat, 0)

    moon_longitude = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)[0][0]
    birth_nakshatra, birth_pada, dasa_table = generate_dasa_table(
        jd, moon_longitude)

    return {
        "birth_nakshatra": birth_nakshatra,
        "birth_pada": birth_pada,
        "dasa_table": dasa_table
    }

# ---------------- YOGAS ----------------
@app.get("/yogas")
def yogas(dob: str, tob: str, lat: float, lon: float, tz_offset: float = 5.5):
    """Detects yogas and doshas in the chart."""
    data, _, _ = get_planet_positions(dob, tob, lat, lon, tz_offset)
    yogas_list = detect_yogas(data)
    return {"yogas": yogas_list}

# ---------------- LIFE PURPOSE ----------------
@app.get("/life_purpose")
def life_purpose(dob: str,
                 tob: str,
                 lat: float,
                 lon: float,
                 tz_offset: float = 5.5,
                 name: str = "User"):
    """Endpoint for life purpose analysis using Vedic astrology."""
    try:
        data, asc_deg, cusps = get_planet_positions(dob, tob, lat, lon,
                                                    tz_offset)
        analysis = analyze_life_purpose(data, asc_deg, cusps)
        report = generate_purpose_report(analysis, data)

        prompt = f"Analyze this life purpose chart for {name}:\n{report}"
        interpretation = ask_gpt(prompt)

        return {
            "chart": data,
            "report": report,
            "interpretation": interpretation
        }
    except Exception as e:
        return {"error": str(e)}

# ---------------- DASA BHRUKTI ----------------
@app.get("/dasa_bhukti")
def dasa_bhukti(dob: str,
                tob: str,
                lat: float,
                lon: float,
                tz_offset: float = 5.5,
                place: str = "Unknown"):
    """
    Detailed Dasa-Bhukti Analysis with GPT interpretation.
    """
    try:
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                        utc_dt.hour + utc_dt.minute / 60.0)

        planet_data, asc_deg, cusps = get_dasa_positions(jd, lat, lon)
        moon_long = planet_data['Moon']['longitude']
        dasa_table = generate_dasa_bhukti_table(jd, moon_long)

        birth_info = {"dob": dob, "tob": tob, "place": place}
        prediction = ask_gpt_dasa_prediction(birth_info, dasa_table,
                                             planet_data)

        return {
            "birth_info": birth_info,
            "planetary_positions": planet_data,
            "dasa_table": dasa_table,
            "gpt_prediction": prediction
        }
    except Exception as e:
        return {"error": str(e)}

# ---------------- SPOUSE ANALYSIS ----------------
@app.get("/spouse")
def spouse_analysis(dob: str,
                    tob: str,
                    lat: float,
                    lon: float,
                    tz_offset: float = 5.5,
                    gender: str = "Male"):
    """
    Endpoint for spouse prediction and marriage analysis.
    """
    try:
        local_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
        utc_dt = local_dt - datetime.timedelta(hours=tz_offset)
        jd = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                        utc_dt.hour + utc_dt.minute / 60.0)

        data, asc_deg = get_spouse_positions(jd, lat, lon)
        aspects = get_spouse_aspects(data, asc_deg)
        analysis = analyze_marriage(data, asc_deg, aspects, gender)
        report = spouse_report(analysis)

        gpt_input = f"Analyze marriage and spouse characteristics:\n{report}"
        interpretation = ask_gpt_spouse(gpt_input)

        return {
            "chart": data,
            "report": report,
            "interpretation": interpretation
        }

    except Exception as e:
        return {"error": str(e)}

# ---------------- INDU DASA ----------------
@app.get("/indu_dasa")
def indu_dasa(dob: str,
              tob: str,
              lat: float,
              lon: float,
              tz_offset: float = 5.5):
    """
    Endpoint for Indu Lagnam-based Dasa & Bhukti timeline.
    """
    try:
        result = get_indu_dasa(dob, tob, lat, lon, tz_offset)
        return result
    except Exception as e:
        return {"error": str(e)}
