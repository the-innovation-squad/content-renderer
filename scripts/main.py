import argparse
from config import Config
cfg = Config()
from video_generator import generate
import os
import shutil

def clear_ouput_directory():
    output_dir = "output"
    file_to_keep = ".gitkeep"
    for item in os.listdir(output_dir):
        item_path = os.path.join(output_dir, item)
        if item != file_to_keep:
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

def configure_args():
    parser = argparse.ArgumentParser(description="Generate a video from a script.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-u", "--upscale", action="store_true", help="Use higher quality generation tools")
    args = parser.parse_args()
    cfg.update_from_args(args)
    cfg.log_args()

def main():
    configure_args()
    clear_ouput_directory()
    generate()

if __name__ == "__main__":
    main()