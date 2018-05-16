'''
Created on Mar 14, 2014

This file contains the expert system skeleton. All the code has been commented in detail
By following the instructions in the comments, it's easy to build a simple one completely
functional expert system.

@author: Viktor Berger
'''
from src import Eparser

############################################################################################
#                                    POMOCNE FUNKCIJE                                      #
############################################################################################

# the function returns a string with the rule in a read-only format,
# odnosno:  IF condition THEN action 
def rule_repr(rule):
    LHS = []
    for attr,values in rule['LHS'].items():
        LHS.append(attr + " = " + "|".join(values))
    for key, elem in rule['RHS'].items():
        (RHSkey,RHSelem) = (key,elem)
        #print(key,elem)
    #(RHSkey,RHSvalue) = rule['RHS'].items()[0]
    
    return "IF " + " & ".join(LHS) + " THEN " + RHSkey + " = " + RHSelem

# Funkcija ispisuje radnu memoriju
def printRM():
    print ("Radna memorija:")
    for r,v in RM.items():
        print (r, " = ", v)

# Funkcija vraca listu svih konfliktnih pravila, odnosno pravila cija desna strana 
# izvodi vrijednost danog parametra
def getConflictRules(rules,goal):
    ruleset = []
    for rule in rules:
        attribute = rule['RHS'].keys()[0]
        if attribute == goal:
            ruleset.append(rule)            
    return ruleset

# Funkcija provjerava postoji li barem jedno pravilo cija desna strana 
# izvodi vrijednost danog cilja
def conflictRuleExists(rules,goal):
    for rule in rules:
        attribute = rule['RHS'].keys()[0]
        if attribute == goal:
            return True        
    return False


# Funkcija provjerava da li dano pravilo pali
# Drugim rijecima, ako su svi atributi s lijeve strane pravila u 
# radnoj memoriji i imaju jednake vrijednosti
def ruleWorks(rule,RM):
    conditions = rule['LHS']
    
    for param in conditions:
        if param in RM:
            if RM[param] not in conditions[param]:
                return False
        else:
            return False
    return True

# Funkcija za korisnicki unos zadanog parametra u radnu memoriju
# Zahtjeva unos dok korisnik ne unese jedan od dopustenih vrijednosti
# Napomena: korisnicki unos moguc je samo za parametre cije ime zavrsava sa znakom '*' 
def parameterInput(param,RM):
    value = input("Molim unesite vrijednost parametra '" + param + "' " + str(parameters[param+"*"]))
    while(value not in parameters[param+"*"]):
        value = input()
    RM[param] = value
    
    
# Funkcija ispisuje atribute/parametre, njihove vrijednosti
# i sva pravila sadrzana u bazi znanja
def printKnowledgeBase(parameters,rules):
    print( '-'*105)
    print ('|' + '\t'*6 + 'The Knowledge Base' + '\t'*6 + '|')
    print ('-'*105 + '\n')
    
    print ("Attribute:")
    for attr,value in parameters.items():
        print (attr + " = " + " | ".join(value))
    
    print ("\nRules:")
    for i,rule in enumerate(rules):
        print (str(i+1) + ") " + rule_repr(rule))
        
    print ('-'*105 + '\n')
       

############################################################################################
#                                    GLAVNI PROGRAM                                        #
############################################################################################

# get attributes and rules from the knowledge base
parameters, rules = Eparser.parse('../base/Rules.txt')

# prints a knowledge base
printKnowledgeBase(parameters, rules)

# work memory, stack with goals and lists of already verified attributes
#whose value can not be exported
RM = {}
goals = []
checked_goals = []


# Ask the user to enter the target hypothesis and save it to the top of that
hipoteza = str(input())
goals.append(hipoteza)

# At the top, therefore, is the hypothesis to prove.
# If the stack is empty then the END.
# The main loop
while(True):

    # If the stack is empty, he has left the loop
    if len(goals) == 0: break
    # pomocne kontrolne varijable
    new_goal = False
    new_parameter = False

    # save the target goal in the variable goal
    goal = goals.pop()

    # create a set of conflict rules and store their number
    KR = getConflictRules(rules,goal)
    KN = len(KR)

    # if no conflicting rule has been found, terminate the loop and notify the user

    # prints a set of conflict rules and state of the working memory

    # A loop passes through a set of conflict rules
    # If the rule is set to:
    # 1) Remove your current goal from the top of that
    # 2) stored on its right side in the working memory
    # 3) put the new_goal variable in True and quit the loop

    # If the rule falls, go to the next goal

    # for each rule in a set of conflict rules

    # If there is a new goal, it gets out of the loop

    # Reduce the number of remaining unsupported rules

    # for each policy parameter currently being checked

    # if the parameter was already checked and it was not possible to perform it,
    # skip rule (do not check other parameters)

    # if the current parameter is in the working memory
    # The parameter value does not match the value in the working memory

    # parameter is not in memory
    # If one of the rules executes the current parameter, set it to the target

    # None of the rules executes the parameter
    # if possible (parameter name ending with '*'),
    # prompts user to input parameter value

    # parameter can not be exported from any rule i
    # user can not enter it (put it in a list of verified goals)

    # if a new parameter is entered, re-check the rules (looping)

    # If no new goal is set and all the rules are checked, remove the goal from the top
    # and store it in a list of goals that can not be achieved
    break  
    print ('-'*100)
                    
                    
print ('*'*48 + "KRAJ RADA" + '*'*48)
                    
    
    
    