import os

def safe_load_env_var(key):
    value = os.getenv(key)
    if value is None:
        raise Exception(f"Environment variable {key} is not set")
    return value

config = {
    "debug": False,
    "ELEVENLABS_API_KEY": safe_load_env_var("ELEVENLABS_API_KEY")
}