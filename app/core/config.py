from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
LITESTAR_PORT = int(os.getenv("LITESTAR_PORT", 8003))