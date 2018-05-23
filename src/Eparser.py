'''
A file parsing program for parsing Rules.txt
'''

import copy
import itertools

def parse(path):
    parameters = {}
    rules = []
    try:
        with open(path,'r') as f:
            lines = f.readlines()        
    except:
        print ("The problem with parsing the file " + path)
        return
    
    for line in lines:
        if not line or line.startswith('-') or line.startswith('#') or line.startswith('\n'):
            continue
        elif line.startswith('IF'):
            current = {}
            sides = line.replace('IF','').split('THEN')
            current['LHS'] = {}
            
            conditions = sides[0].split('&')
            for condition in conditions:
                ruleList = list(map(str.strip, condition.split('=', 1)))

                for a, b in itertools.combinations(ruleList, 2):
                    current['LHS'][a] = [s.strip() for s in b.split('|')]

            action = sides[1]
            actionList = list(map(str.strip, action.split('=')))
            for a, b in itertools.combinations(actionList, 2):
                current['RHS'] = {a:b}
            rules.append(copy.deepcopy(current))
        else:
            splitLine = line.split('=',1)
            parameters[splitLine[0].strip()] = [s.strip() for s in splitLine[1].split('|')]    
            
    return parameters, rules
     
        
    