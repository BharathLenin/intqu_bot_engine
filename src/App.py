from flask import Flask, render_template, request
from src import RuleEngine
from urllib import parse


app = Flask(__name__)

@app.route('/')
def index():
    #return render_template('test.html')
    return "Welcome to Inference Engine!"

@app.route('/getKnowledgeBase/<statement>')
def getKnowlegdeBase(statement):
    print(statement)
    #statement = request.form['statement']
    action = RuleEngine.fetchRuleByStatement(statement);
    return '%s' %(action)

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000)