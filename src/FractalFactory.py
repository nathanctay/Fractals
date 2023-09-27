from Fractal import Mandelbrot, Julia, BurningShipJulia
from FractalParser import parse

def makeFractal(info):
    # info = parse(file)
    if info['type'] == 'mandelbrot':
        fractal = Mandelbrot(info)
    elif info['type'] == 'julia':
        fractal = Julia(info)
    elif info['type'] == 'burningshipjulia':
        fractal = BurningShipJulia(info)
    else:
        raise NotImplementedError("Not a valid fractal type")
    return fractal
