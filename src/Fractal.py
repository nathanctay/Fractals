from FractalParser import parse


class Fractal:
    def __init__(self, info):
        self.pixels = info['pixels']
        self.iterations = info['iterations']
        self.min = {'x': info['centerx'] - info['axislength'] / 2, 'y': info['centery'] - info['axislength'] / 2}
        self.max = {'x': info['centerx'] + info['axislength'] / 2, 'y': info['centery'] + info['axislength'] / 2}
        self.axislength = info['axislength']
        self.pixelsize = self.axislength / self.pixels

        # raise NotImplementedError("Can't have just a blank fractal")

    def count(self, complexNum):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

    def getPixels(self):
        return self.pixels

    def getIterations(self):
        return self.iterations

    def getMinX(self):
        return self.min['x']

    def getMinY(self):
        return self.min['y']

    def getMaxX(self):
        return self.max['x']

    def getMaxY(self):
        return self.max['y']

    def getAxisLength(self):
        return self.axislength

    def getPixelSize(self):
        return self.pixelsize

class Julia(Fractal):
    def __init__(self, info):
        super().__init__(info)
        self.cReal = info['creal']
        self.cImag = info['cimag']

    def count(self, z):
        """Return the iteration count for this part of the Julia fractal Complex Plane"""

        # c is the Julia Constant; varying this value can yield interesting images
        c = complex(self.cReal, self.cImag)

        for i in range(self.iterations - 1):
            z = z * z + c  # Iteratively compute z1, z2, z3 ...
            if abs(z) > 2.0:
                return i
        return self.iterations - 1

class Mandelbrot(Fractal):
    def __init__(self, info):
        super().__init__(info)
    def count(self, c):
        """Return the iteration count of the Mandelbrot set at this point in the complext plane"""
        z = complex(0, 0)  # z0

        for i in range(self.iterations - 1):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2.0:
                return i  # The sequence is unbounded

        return self.iterations - 1


class BurningShipJulia(Fractal):
    def __init__(self, info):
        super().__init__(info)
        self.cReal = info['creal']
        self.cImag = info['cimag']

    def count(self, z):
        """Return the iteration count for this point of the Burning Ship Julia fractal Complex Plane"""
        c = complex(self.cReal, self.cImag)

        for i in range(self.iterations - 1):
            z = complex(abs(z.real), abs(z.imag))
            z = z ** 2 - c
            if abs(z) > 2.0:
                return i

        return self.iterations - 1


