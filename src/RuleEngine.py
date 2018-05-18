'''
This file contains the expert system skeleton. All the code has been commented in detail
By following the instructions in the comments, it's easy to build a simple one completely
functional expert system.

'''
from src import Eparser

# the function returns a string with the rule in a read-only format,
# odnosno:  IF condition THEN action
def rule_repr(rule):
    LHS = []
    for attr, values in rule['LHS'].items():
        LHS.append(attr + " = " + "|".join(values))
    for key, elem in rule['RHS'].items():
        (RHSkey, RHSelem) = (key, elem)
        # print(key,elem)
    # (RHSkey,RHSvalue) = rule['RHS'].items()[0]

    return "IF " + " & ".join(LHS) + " THEN " + RHSkey + " = " + RHSelem


# The function returns a list of all conflicting rules, ie the rules of the right side
# performs the value of a given parameter

def getMatchingRules(rules, statement):
    ruleset = []
    for rule in rules:
        a=0
        for key, value in rule['LHS'].items():
            att = ''.join(value)
            if '*' in att:
                att = att[1:]
                if att not in statement:
                #print('attribute value '+att)
                    a+=1
            else:
                if att in statement:
                #print('attribute value '+att)
                    a+=1
        if a==len(rule['LHS']):
            ruleset.append(rule)
    return ruleset

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

    # work memory, stack with goals and lists of already verified attributes
    # whose value can not be exported
    RM = {}
    goals = []
    checked_goals = []

    # Request the user to enter the target hypothesis
    #goal = input('Enter the Statement: ')
    goals.append(goal)

    # At the top, therefore, is the hypothesis to prove.
    # If the stack is empty then the END.
    # The main loop
    while (True):

        # If the stack is empty, he has left the loop
        if len(goals) == 0: break
        # pomocne kontrolne varijable
        new_goal = False
        new_parameter = False

        # save the target goal in the variable goal
        goal = goals.pop()

        # create a set of conflict rules and store their number
        matchingRules = getMatchingRules(rules, goal)
        noOfMatchingRules = len(matchingRules)

        if noOfMatchingRules == 0:
            print('Too little data')
            break

        print('Matching Rules:')
        for cr in matchingRules:
            print(rule_repr(cr))
            action = getMatchingRuleAction(matchingRules)
            print(action)


        break
        print('-' * 100)

    print('*' * 48 + "END OF WORK" + '*' * 48)
    return action


