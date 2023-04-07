import argparse
from generator import generate
from config import Config
cfg = Config()

def configureArgs():
    parser = argparse.ArgumentParser(description="Example of using flags in Python")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable the flag")
    args = parser.parse_args()
    cfg.set_debug(args.debug)

def main():
    generate()


if __name__ == "__main__":
    main()