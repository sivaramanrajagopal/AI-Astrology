import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Configuration - Use environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Validate API key is present
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")

# Set the environment variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 