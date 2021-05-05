import argparse
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import src.app
import src.dots_square
import src.dots_hexagonal
import src.lines
import src.circles
import src.squares
import src.shared_constants as sc


parser = argparse.ArgumentParser()
parser.add_argument(
    "name",
    nargs="?",
    default="dots_square",
    help="Name of the particle simulation."
)
parser.add_argument(
    "-w",
    "--window-size",
    metavar=("<width>", "<height>"),
    nargs=2,
    type=int,
    default=sc.WINDOW_SIZE,
    help="Specify the window width and height in pixels."
)
args = parser.parse_args()

patterns = {
    "dots_square": src.dots_square.DotsSquarePattern,
    "dots_hexagonal": src.dots_hexagonal.DotsHexagonalPattern,
    "lines": src.lines.LinePattern,
    "circles": src.circles.CirclesPattern,
    "squares": src.squares.SquarePattern
}
if args.name not in patterns:
    parser.error(f"name must be one of {list(patterns)}")

sc.WINDOW_SIZE = args.window_size

src.app.App(patterns, args.name).run()
