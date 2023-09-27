def parse(infoFile = ""):
    fractalInfo = {
        'type': "julia",
        'pixels': 512,
        'iterations':78,
        'centerx': -1.01537721564149,
        'centery': 0.249425427273733,
        'axislength':0.0121221433855615,
        'creal': -1,
        'cimag': 0}

    if infoFile != "":
        info = open(infoFile)
        lines = info.readlines()
        for line in lines:
            line = line.split(':')
            if line[0] in fractalInfo:
                if line[1].strip().isnumeric():
                    fractalInfo[line[0]] = int(line[1].strip())
                elif line[1].strip().isalpha():
                    fractalInfo[line[0]] = line[1].strip().lower()
                else:
                    fractalInfo[line[0]] = float(line[1].strip())
        if fractalInfo['type'] == 'julia' or fractalInfo['type'] == 'burningshipjulia':
            crealFound = False
            cimagFouns = False

    return fractalInfo
