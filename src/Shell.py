'''
Created on Mar 14, 2014

Simple expert system.

@author: Viktor Berger
'''
from src import Eparser

############################################################################################
#                                    POMOCNE FUNKCIJE                                      #
############################################################################################


# function returns a string with a read-only rule,
# or: IF condition THEN action
def rule_repr(rule):
    LHS = []
    for attr,values in rule['LHS'].items():
        LHS.append(attr + " = " + "|".join(values))
    for key, elem in rule['RHS'].items():
        (RHSkey,RHSelem) = (key,elem)
    #(RHSkey,RHSvalue) = rule['RHS'].items()[0]
    
    return "IF " + " & ".join(LHS) + " THEN " + RHSkey + " = " + RHSelem

#The function prints the operating memory
def printRM():
    print ("Radna memorija:")
    for r,v in RM.items():
        print (r, " = ", v)


# The function returns a list of all conflicting rules, ie the rules of the right side
# performs the value of a given parameter
def getConflictRules(rules,goal):
    ruleset = []
    for rule in rules:
        attribute = rule['RHS'].keys()[0]
        if attribute == goal:
            ruleset.append(rule)            
    return ruleset


# The function returns a list of all conflicting rules, ie the rules of the right side
# performs the value of a given parameter
def conflictRuleExists(rules,goal):
    for rule in rules:
        attribute = rule['RHS'].keys()[0]
        if attribute == goal:
            return True        
    return False



# The function checks if the given rule is set to fire
# In other words, if all the attributes on the left side of the rule are in
# work memory and have the same values
def ruleWorks(rule,RM):
    conditions = rule['LHS']
    
    for param in conditions:
        if param in RM:
            if RM[param] not in conditions[param]:
                return False
        else:
            return False
    return True


# User input function of the default parameter in the working memory
# Requests entry until the user inputs one of the permissible values
# Note: A user input is only possible for parameters whose name ends with the '*'
def parameterInput(param,RM):
    value = input("Please enter a parameter value '" + param + "' " + str(parameters[param+"*"]))
    while(value not in parameters[param+"*"]):
        value = input()
    RM[param] = value
    
    
# Function prints attributes / parameters, their values
# and all rules contained in the knowledge base
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



# The shape of the stair is initially composed of the most important goals (hypotheses) to prove

# Zatrazi korisnika unos ciljne hipoteze
goal = input('Unesi hipotezu: ')
goals.append(goal)

# Na vrhu stoga je hipoteza koju treba dokazati.Ako je stog prazan, onda je KRAJ

# Glavna petlja
while(True):
    
    # ako je stog prazan, izadi iz petlje
    if len(goals) == 0:
        break
    
    # pomocne kontrolne varijable
    new_goal = False
    new_parameter = False 
    
    # pohrani trnutni cilj u varijablu goal
    goal = goals[-1]
 
    # stvori skup konfliktnih pravila i pohrani njihov broj
    conflictRules = getConflictRules(rules,goal)
    remainingRules = len(conflictRules)
    
    # ako nije pronadeno nijedno konfliktno pravilo prekini petlju i obavijesti korisnika
    if remainingRules == 0:
        print ('Premalo podataka')
        break
    
    # ispisi skup konfliktnih pravila i stanje radne memorije
    print ('Konfliktna pravila: ')
    for cr in conflictRules:
        print (rule_repr(cr))
    printRM()
    
    # U petlji prolazi kroz skup konfliktnih pravila      
    # Ako pravilo pali:
    # 1) skini trenutni cilj s vrha stoga
    # 2) pohrani njegovu desnu stranu u radnu memoriju
    # 3) postavi varijablu new_goal u True i izadi iz petlje
    for cr in conflictRules:
        if ruleWorks(cr,RM):
            (RHSkey,RHSvalue) = cr['RHS'].items()[0]
            RM[RHSkey] = RHSvalue
            curr_goal = goals.pop()
            print ("Ostvaren je cilj: "  + curr_goal + " = " + RHSvalue)
            new_goal = True
            break
    
    # Ako je idi na iduci cilj
    if new_goal:
        continue   
        
    # za svako pravilo u skupu konfliktnih pravila
    for cr in conflictRules:
        
        # ako je new_goal True, izadji iz petlje
        if new_goal :
            break
        
        # smanji broj preostalih neprovjerenih pravila
        remainingRules -= 1
        conditions = cr['LHS']
        
        # za svaki parametar pravila koje se trenutno provjerava
        for param in conditions:
            # ako je parametar vec provjeren i nije ga bilo moguce izvesti, 
            # preskoci pravilo (ne provjeravaj ostale parametre )
            if param in checked_goals:
                break
            # ako je trenutni parametar u radnoj memoriji
            if param in RM:
                # vrijednost parametra se ne podudara s vrijednoscu koja je u radnoj memoriji
                if RM[param] not in conditions[param]:
                    break
            else: # parametar nije u memoriji
                # ako neko od pravila izvodi trenutni parametar, postavi ga za cilj
                if conflictRuleExists(rules,param): 
                    goals.append(param)
                    new_goal = True
                    break                
                elif param + "*" in parameters: 
                    # Nijedno od pravila ne izvodi parametar 
                    # ako je moguce(ime parametra zavrsava sa znakom '*'), 
                    # trazi korisnika za unos vrijednosti parametra
                    parameterInput(param,RM)
                    new_parameter = True
                    break
                else:
                    # parametar se ne moze izvesti iz nekog od pravila i 
                    # korisnik ga ne moze unesti
                    checked_goals.append(param)
        
        # ako je unesen novi parametar, ponovno provjeri pravila (izadji iz petlje)
        if new_parameter:
            break
                    
        # ako nije postavljen novi cilj i sva su pravila provjerena, skini cilj s vrha stoga
        # i pohrani ga u listu ciljeva koji se ne mogu ostvariti
        if remainingRules == 0 and not new_goal:
            curr_goal = goals.pop()
            checked_goals.append(curr_goal)
            print ('Neostvarivi cilj: ' + curr_goal)
            
    print ('-'*100)
                    
                    
print ('*'*48 + "KRAJ RADA" + '*'*48)
                    
    
    
    