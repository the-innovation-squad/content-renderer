import os

def get_env_var(key):
    value = os.getenv(key)
    if value is None:
        raise Exception(f"Environment variable {key} is not set")
    return value

config = {
    "debug": False,
    "ELEVENLABS_API_KEY": get_env_var("ELEVENLABS_API_KEY")
}