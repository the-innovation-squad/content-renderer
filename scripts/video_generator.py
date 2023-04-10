import os
import yaml
from video import create_segment, concatenate_segments
from narration import create_narration

def generate():
    print("> Reading input files...")
    with open("input/video_script.yml", "r") as file:
        video_script = yaml.safe_load(file)

    global_engine = video_script.get("engine", "google")

    # Iterate through the timeline of content items and stock video clips to create video segments
    for index, item in enumerate(video_script["timeline"]):
        print(f"> Processing scene {index + 1} of {len(video_script['timeline'])}...")
        content = item["content"]
        clip_url = item["clip"]

        narration_options = {
            "engine": item.get("engine", global_engine),
        }
        video_options = {
            "captions": video_script.get("captions", False),
            "watermark_url": video_script.get("watermark", False)
        }

        output_dir = "output/" + str(index)
        os.mkdir(output_dir)

        print("> Creating narration...")
        audio_file_path = create_narration(content, narration_options, output_dir)
        print("> Compiling video segment...")
        create_segment(audio_file_path, clip_url, content, video_options, output_dir)

    # Stitch the video segments together
    segment_paths = [os.path.join("output", str(index), "video_processed.mp4") for index, item in enumerate(video_script["timeline"])]
    concatenate_segments(segment_paths, "output/final.mp4")