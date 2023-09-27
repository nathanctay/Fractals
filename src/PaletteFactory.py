from Palette import Watermelon, LemonLime
def makePalette(paletteType, iterats):
    if paletteType.lower() == 'watermelon':
        palette = Watermelon(iterats)
    elif paletteType.lower() == 'lemonlime':
        palette = LemonLime(iterats)
    elif paletteType == '':
        palette = Watermelon(iterats)
    else:
        raise NotImplementedError("That palette type is not supported")
    return palette
