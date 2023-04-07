import os
import yaml
from video import create_segment, concatenate_segments
from narration import create_narration

def generate():
    # Read the YAML file
    with open("input/video_script.yml", "r") as file:
        video_script = yaml.safe_load(file)

    # Iterate through the timeline of content items and stock video clips to create video segments
    for index, item in enumerate(video_script["timeline"]):
        content = item["content"]
        clip = item["clip"]

        output_path = "output/" + str(index)
        os.mkdir(output_path)
        
        audio = create_narration(content, output_path)
        create_segment(audio, clip, output_path)

    # Stitch the video segments together
    segment_paths = [os.path.join("output", str(index), "video_processed.mp4") for index, item in enumerate(video_script["timeline"])]
    concatenate_segments(segment_paths, "output/final.mp4")

    # TODO: add watermark at the end if one is provided

