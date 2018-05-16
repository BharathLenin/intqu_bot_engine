from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template('test.html')
    return "Welcome!"


@app.route('/getKnowledgeBase/<statement>')
def getKnowledgeBase(statement):
    # statement = request.form['statement']

    return '%s' % (statement)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)