'''
Engine which fetches and applies the appropriate rules from Rules.txt
'''

from src import Eparser
from src import DescReader

# the function returns a string with the rule in a read-only format,

def rule_repr(rule):
    LHS = []
    for attr, values in rule['LHS'].items():
        LHS.append(attr + " = " + "|".join(values))
    for key, elem in rule['RHS'].items():
        (RHSkey, RHSelem) = (key, elem)

    return "IF " + " & ".join(LHS) + " THEN " + RHSkey + " = " + RHSelem


# The function returns a list of all matching rules

def getMatchingRules(rules, statement):
    ruleset = []
    for rule in rules:
        a=0
        for key, value in rule['LHS'].items():
            att = ''.join(value)
            if '*' in att:
                att = att[1:]
                if att not in statement:
                    a+=1
            else:
                if att in statement:
                    a+=1
        if a==len(rule['LHS']):
            ruleset.append(rule)
    return ruleset

# The function returns actions of all matching rules from knowledge base
def getMatchingRuleAction(rules):
    for rule in rules:
        for key, value in rule['RHS'].items():
            key = ''.join(key)
            if key == 'action':
                value = ''.join(value)
            else:
                print('No actions defined yet')
    return value

# Function prints attributes / parameters, their values
# and all rules contained in the knowledge base

def printKnowledgeBase(parameters, rules):
    print('-' * 105)
    print('|' + '\t' * 6 + 'The Knowledge Base' + '\t' * 6 + '|')
    print('-' * 105 + '\n')

    print("Attribute:")
    for attr, value in parameters.items():
        print(attr + " = " + " | ".join(value))

    print("\nRules:")
    for i, rule in enumerate(rules):
        print(str(i + 1) + ") " + rule_repr(rule))

    print('-' * 105 + '\n')

def fetchRuleByStatement(goal):

    # get attributes and rules from the knowledge base
    parameters, rules = Eparser.parse('../base/Rules.txt')

    # prints a knowledge base
    printKnowledgeBase(parameters, rules)

    goals = []
    action = ''
    actiondesc = ''
    goals.append(goal)

    # The main loop
    while (True):

        # If the stack is empty, leave he loop
        if len(goals) == 0: break

        # create a set of matching rules and store number of matching rules
        matchingRules = getMatchingRules(rules, goal)
        noOfMatchingRules = len(matchingRules)

        if noOfMatchingRules == 0:
            action = 'No Matching Rules Found'
            print(action)
            break

        print('Matching Rules:')
        for cr in matchingRules:
            print(rule_repr(cr))
            action = getMatchingRuleAction(matchingRules)
            actiondesc = DescReader.fileParse('../base/Description.txt',action)
            print(actiondesc)
        break
        print('-' * 100)

    print('*' * 48 + "END OF WORK" + '*' * 48)
    return action + '     ' + actiondesc


