import itertools

def parse(path):
    try:
        f = open(path, 'r')
        lines = f.readlines()
    except:
        print("The problem with parsing the file " + path)
        return

    for line in lines:
        if not line or line.startswith('-') or line.startswith('#'):
            continue
        elif line.startswith('<'):
            current = {}
            sides = line.replace('<',' ').replace('>',' ').split(' ',1)
            current['LHS'] = {}
            conditions = sides[1].split(' ',1)
            tag = conditions[0]
            myWords = [x for x in conditions[1].split()]
            #print(myWords)
            for condition in myWords:
                ruleList  = list(map(str.strip, condition.split('=')))
                if(len(ruleList) == 2):
                    for a, b in itertools.combinations(ruleList, 2):
                        current['LHS'][a] = 'IF tag = '+ tag + ' & attr = *'+ ruleList[0] + ' THEN action = Add '+ ruleList[0]
            #print (current['LHS'])
        else:
            print('do nothing')

    return current['LHS']