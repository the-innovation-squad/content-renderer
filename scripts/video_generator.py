import os
import yaml
from video import create_segment, concatenate_segments
from narration import create_narration
from concurrent.futures import ThreadPoolExecutor

def process_scene(index, item, video_script, global_engine, global_engine_settings):
    print(f"> Processing scene {index + 1} of {len(video_script['timeline'])}...")
    content = item["content"]
    clip_url = item["clip"]

    narration_options = {
        "engine": item.get("engine", global_engine),
        "engine_settings": item.get("engine_settings", global_engine_settings)
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

def generate():
    print("> Reading input files...")
    with open("input/video_script.yml", "r") as file:
        video_script = yaml.safe_load(file)

    global_engine = video_script.get("engine", "google")
    global_engine_settings = video_script.get("engine_settings", {})

    # Iterate through the timeline of content items and stock video clips to create video segments
    with ThreadPoolExecutor() as executor:
        executor.map(
            process_scene,
            range(len(video_script["timeline"])),
            video_script["timeline"],
            [video_script] * len(video_script["timeline"]),
            [global_engine] * len(video_script["timeline"]),
            [global_engine_settings] * len(video_script["timeline"]),
        )

    print("> Concatenating video segments...")
    segment_paths = [os.path.join("output", str(index), "video_processed.mp4") for index, item in enumerate(video_script["timeline"])]
    concatenate_segments(segment_paths, "output/final.mp4")
    print("> Done.")