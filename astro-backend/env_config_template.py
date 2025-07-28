import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Configuration - Use environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate API key is present
if not OPENAI_API_KEY:
    print("WARNING: OPENAI_API_KEY environment variable is not set!")
    print("Please set your OpenAI API key in the environment variables.")
    OPENAI_API_KEY = "your_openai_api_key_here"  # Fallback for development

# Set the environment variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 