import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# get api key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")