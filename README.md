An interactive exploration of [Moiré patterns](https://en.wikipedia.org/wiki/Moir%C3%A9_pattern). They appear when an image with transparent gaps is moved and rotated in front of another image with a similar pattern.

Concentric circles displaced relative to each other:  
![circles example](images/circles.png)

Dots arranged in a square grid, one of the grids slightly rotated:  
![dots example](images/dots.png)

Requires Python 3 and Pygame 2. You can choose the pattern by giving its name as the first argument.
If it is missing, the "dots" pattern is used.
```
python moire.py lines
```
Available patterns:
- dots
- lines
- circles


### Controls:
Action | Binding
--- | ---
Move | Left mouse button or W, A, S, D
Rotate | Right mouse button or Q, E
Reset | Backspace
Toggle info display | F1
Quit | Esc


### Command Line Arguments
- -w, --window-size \<width> \<height>: Specify the window width and height in pixels.
- -h, --help: Show a help message and exit.
