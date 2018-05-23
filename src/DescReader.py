'''
This file is to read the description from Description.txt
'''


def fileParse(path,action):
    try:
        f = open(path, 'r')
        lines = f.readlines()
    except:
        print("The problem with parsing the file " + path)
        return

    #print(lines)

    for line in lines:
        if not line or line.startswith('-') or line.startswith('#') or line.startswith('\n'):
            continue
        else:
            sides = line.split('=', 1)
            #print(sides)
            LHS = ''.join(sides[0]).strip()
            if LHS ==action:
                actionDesc = ''.join(sides[1]).strip()
            else:
                actionDesc = ' '
    return actionDesc
