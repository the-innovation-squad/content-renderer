import os
from parse_script import parse
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ["ELEVEN_LABS_API_KEY"]

    parse(api_key)