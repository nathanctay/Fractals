# Fractal Visualizer User Manual

This program is run from the command line.

You will run the main.py program and add the fractal file name and palette name as arguments.
(ex: python3 main.py hourglass.frac watermelon)

All files should have the fractal type, the center x value, the center y value, the axis length, the width of the image in pixels,
and how many iterations it should run for the color

Julia fractals should also include the real and imaginary components for c (creal and cimag).

The supported fractal types are julia, mandelbrot, and burning ship julia

The supported palettes are watermelon and lemonlime.

If you leave out the palette name it will default to watermelon.

If you leave out both the palette name and the fractal file, it will default to a lace-curtains fractal with a watermelon paleette

If you provide an unsupported palette, or an unsupported fractal type, the program will quit.

Once given a correct file, the program will display it to the screen, and save it as a .png to whatever your location is.