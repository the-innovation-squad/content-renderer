import os
import yaml
from video import create_segment, concatenate_segments
from narration import create_narration
from concurrent.futures import ThreadPoolExecutor

def process_scene(index, timeline_entry, settings):
    content = timeline_entry["content"]
    clip_url = timeline_entry["clip"]

    global_engine = settings.get("engine", "google")
    global_engine_settings = settings.get("engine_settings", {})

    narration_options = {
        "engine": timeline_entry.get("engine", global_engine),
        "engine_settings": timeline_entry.get("engine_settings", global_engine_settings)
    }
    video_options = {
        "captions": settings.get("captions", False),
        "watermark_url": settings.get("watermark", False),
        "resolution": settings.get("resolution", "1920, 1080")
    }

    output_dir = "output/" + str(index)
    os.mkdir(output_dir)

    audio_file_path = create_narration(content, narration_options, output_dir)
    create_segment(audio_file_path, clip_url, content, video_options, output_dir)

def generate():
    print("> Reading input files...")
    with open("input/script.yml", "r") as file:
        script = yaml.safe_load(file)
    with open("input/settings.yml", "r") as file:
        settings = yaml.safe_load(file)

    # Iterative approach since thread pool executor is saving audio to clips with errors
    for index, item in enumerate(script["timeline"]):
        print(f"> Processing scene {index + 1} of {len(script['timeline'])}...")
        process_scene(index, item, settings)
    # Commented out due to audio errors, in videos with > 1 scene, audio is cut off in some scenes when saving to file
    # TODO: investigate this 🤔
    # print("> Processing scenes concurrently...")
    # scene_count = len(script["timeline"])
    # with ThreadPoolExecutor() as executor:
    #     executor.map(
    #         process_scene,
    #         range(scene_count),
    #         script["timeline"],
    #         [settings] * scene_count
    #     )

    print("> Concatenating video segments...")
    segment_paths = [os.path.join("output", str(index), "video_processed.mp4") for index, item in enumerate(script["timeline"])]
    concatenate_segments(segment_paths, "output/final.mp4")
    print("> Done.")