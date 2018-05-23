from flask import Flask, request
from src import RuleEngine
from src import RuleWriter


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Inference Engine!"


@app.route('/getKnowledgeBase')
def getKnowledgeBase():
    statement = request.args.get('statement')
    mode = request.args.get('mode')
    if mode == 'expert':
       print('mode1')
       RuleWriter.createRules(statement)
       action = 'Success'
    else:
        print('mode2')
        action = RuleEngine.fetchRuleByStatement(statement)
    return '%s' %(action)

@app.route('/updateUserProfile')
def updateUserProfile():
    name = request.args.get('name')
    experience = request.args.get('experience')
    technology = request.args.get('technology')
    responsive = request.args.get('responsive')
    lingual = request.args.get('lingual')
    mode = request.args.get('mode')
    f = open('../base/Users.txt', 'a')
    f.write(name + "\t" + experience + "\t" +  technology + "\t" + responsive + "\t" + lingual + "\t" +  mode)
    f.write("\n")
    f.close()
    return 'Hello %s , we saved your information' %(name)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000)