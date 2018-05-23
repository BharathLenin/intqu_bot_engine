'''
File to write new rules to knowledge base
'''

from src import RuleComparator
from src import RuleInputReader

def createRules(statement):
    printRuleToWrite = ''
    f = open('../base/RuleInput.txt', 'w')
    f.write(statement)
    f.close()
    existingRules = RuleComparator.getExistingRules('../base/Rules.txt')
    #print(existingRules)
    ruleInput = RuleInputReader.parse('../base/RuleInput.txt')
    ruleToWrite = RuleComparator.compareExistAndNewRule(ruleInput, existingRules)
    #print(ruleToWrite)
   # printRuleToWrite = '\n'
    for rule in ruleToWrite:
        printRuleToWrite =  printRuleToWrite + rule +'\n'
    print (printRuleToWrite)
    f = open('../base/Rules.txt','a')
    f.write(printRuleToWrite)
    f.close()