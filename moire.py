import argparse
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import src.app
import src.dots
import src.lines
import src.circles


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

patterns = {
    "dots": src.dots.DotsPattern,
    "lines": src.lines.LinePattern,
    "circles": src.circles.CirclesPattern
}
if args.name not in patterns:
    parser.error(f"name must be one of {list(patterns)}")

src.app.App(patterns, args.name, args.window_size).run()
