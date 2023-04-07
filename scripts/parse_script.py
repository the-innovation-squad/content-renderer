import yaml
from voice import generate_voice_recording
from video import create_video

# Main function to parse the YAML file and call the create_content and create_video functions
def parse():
    # Read the YAML file
    with open('input/video_script.yml', 'r') as file:
        video_script = yaml.safe_load(file)

    # Iterate through the timeline of content items and stock video clips
    for item in video_script['timeline']:
        content = item['content']
        clip = item['clip']

        audio = generate_voice_recording(content)
        create_video(audio, clip)