from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.jinja2', messages=messages)

@app.route('/post/add', methods=['POST'])
def add_post():
    text = request.form.get('text')
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    messages.append({'text': text, 'timestamp': timestamp})
    return 'Message added.'

if __name__ == '__main__':
    app.run(debug=True)

