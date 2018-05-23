'''
This file is to compare the existing rules in Rules.txt with the new rule generated from expert input.
If new rule not exists in Rules.txt then will add up to it.
'''

def getExistingRules(path):
    sides = []
    extRule = []
    f = open(path, 'r')
    lines = f.readlines()

    for line in lines:
        if line.startswith('IF'):
            sides.append(line.split('\n', 1))

    for value in sides:
        for rule in value:
            if rule != '':
                extRule.append(rule)
    #print(extRule)
    f.close()
    return extRule


def compareExistAndNewRule(ruleInput,existingRules):

    ruleToWrite = []
    for items in ruleInput.values():
        count = 0
        for rule in existingRules:
            if rule == items:
                print('Rule: ('+ rule +') already exists')
                break
            else:
                count += 1
        if count == len(existingRules):
            ruleToWrite.append(items)

    return ruleToWrite
