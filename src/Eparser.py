'''
A file parsing program that contains expert system knowledge.

The files consist of rules and attributes.
Rule format and attributes in files:

attributes:
    In the file: NameAtributa1 (*) = value1 | value2 | ...
    In the memory: {'ImeAtributa1 (*)': ['vijednost1', 'vrijednost2', ...], ...}

Rules:
    In the file: IF attribute1 = value1 | value2 | ... & attribute2 = value1 | value2 | ... THEN attribute = value
    In the memory: {'LHS': {'attribute1': ['value1', 'value2', ...], 'attribute2': ['value1', 'value2']}
                  'RHS': {'attribute': 'value'}}

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
        if not line or line.startswith('-') or line.startswith('#'):
            continue
        elif line.startswith('IF'):
            current = {}
            sides = line.replace('IF','').split('THEN')
            current['LHS'] = {}
            
            conditions = sides[0].split('&')
            for condition in conditions:
                ruleList = list(map(str.strip, condition.split('=', 1)))

                for a, b in itertools.combinations(ruleList, 2):
                # print (a)
                    current['LHS'][a] = [s.strip() for s in b.split('|')]
                #compare(a, b)


            action = sides[1]
            actionList = list(map(str.strip, action.split('=')))
            for a, b in itertools.combinations(actionList, 2):
                current['RHS'] = {a:b}
            rules.append(copy.deepcopy(current))
        else:
            splitLine = line.split('=',1)
            parameters[splitLine[0].strip()] = [s.strip() for s in splitLine[1].split('|')]    
            
    return parameters, rules
     
        
    