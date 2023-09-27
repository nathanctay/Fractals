# 4.  `Palette.py`
#     *   A color palette is an array of colors; colors are simple strings
#     *   This file will contain two color palettes
#     *   The following statements hold true for a color palette named `P`:
#         *   When the Mandelbrot or Julia fractal function returns an **iteration count** of a point in the complex plane, the corresponding pixel is painted the color of `P[count]`
#         *   Your program should never allow `count >= len(P)`
from colour import Color
from math import ceil


class Palette:
    def __init__(self ,iterations):
        self.palette = []

    def getColor(self, n):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")


class Watermelon(Palette):
    def __init__(self, iterations):
        super().__init__(iterations)
        iters = ceil(iterations/8)
        red = Color('red')
        green = Color('green')
        black = Color('black')
        cyan = Color('cyan')
        pink = Color('pink')
        magenta = Color('magenta')
        for c in green.range_to(red, iters):
            self.palette.append(c.hex_l)
        for c in red.range_to(black, iters):
            self.palette.append(c.hex_l)
        for c in black.range_to(cyan, iters):
            self.palette.append(c.hex_l)
        for c in cyan.range_to(magenta, iters):
            self.palette.append(c.hex_l)
        for c in magenta.range_to(green, iters):
            self.palette.append(c.hex_l)
        for c in green.range_to(pink, iters):
            self.palette.append(c.hex_l)
        for c in pink.range_to(cyan, iters):
            self.palette.append(c.hex_l)
        for c in cyan.range_to(green, iters):
            self.palette.append(c.hex_l)

    def getColor(self, n):
        return self.palette[n]


class LemonLime(Palette):
    def __init__(self, iterations):
        super().__init__(iterations)
        iters = ceil(iterations/8)
        turquoise = Color('turquoise')
        yellow = Color('yellow')
        gray = Color('gray')
        blue = Color('blue')
        lime = Color('lime')
        magenta = Color('magenta')
        for c in turquoise.range_to(yellow, iters):
            self.palette.append(c.hex_l)
        for c in yellow.range_to(gray, iters):
            self.palette.append(c.hex_l)
        for c in gray.range_to(lime, iters):
            self.palette.append(c.hex_l)
        for c in lime.range_to(blue, iters):
            self.palette.append(c.hex_l)
        for c in blue.range_to(yellow, iters):
            self.palette.append(c.hex_l)
        for c in yellow.range_to(magenta, iters):
            self.palette.append(c.hex_l)
        for c in magenta.range_to(blue, iters):
            self.palette.append(c.hex_l)
        for c in blue.range_to(turquoise, iters):
            self.palette.append(c.hex_l)

    def getColor(self, n):
        return self.palette[n]
