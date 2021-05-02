import argparse
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import src.run


parser = argparse.ArgumentParser()
parser.add_argument(
    "name",
    nargs="?",
    default="dots",
    help="Name of the particle simulation."
)
parser.add_argument(
    "-w",
    "--window-size",
    metavar=("<width>", "<height>"),
    nargs=2,
    type=int,
    default=(1200, 800),
    help="Specify the window width and height in pixels."
)
args = parser.parse_args()

valid_names = {"dots", "lines"}
if args.name not in valid_names:
    parser.error(f"name must be one of {list(valid_names)}")

src.run.run(args.name, args.window_size)
