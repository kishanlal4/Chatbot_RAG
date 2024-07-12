#For loading environment variables
import os
from dotenv import load_dotenv

load_dotenv(".env")

#openai
openai_key = os.environ.get("openai_key")


