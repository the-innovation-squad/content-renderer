import os
import yaml
from video import create_segment
from narration import create_narration

def generate():
    # Read the YAML file
    with open("input/video_script.yml", "r") as file:
        video_script = yaml.safe_load(file)

    # Iterate through the timeline of content items and stock video clips to create video segments
    for index, item in enumerate(video_script["timeline"]):
        content = item["content"]
        clip = item["clip"]

        os.mkdir("output/" + str(index))
        narration_output_file = "output/" + str(index) + "/narration.mpeg"
        video_output_file = "output/" + str(index) + "/video.mp4"

        audio = create_narration(content, narration_output_file)
        create_segment(audio, clip, video_output_file)

    # Stitch the video segments together

