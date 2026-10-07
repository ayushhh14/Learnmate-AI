import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

CHROMA_PATH = "data/chroma"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

TOP_K = 5