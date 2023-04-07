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
    parser = argparse.ArgumentParser(description="Example of using flags in Python")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable the flag")
    args = parser.parse_args()
    cfg.set_debug(args.debug)

def main():
    configure_args()
    clear_ouput_directory()
    generate()

if __name__ == "__main__":
    main()