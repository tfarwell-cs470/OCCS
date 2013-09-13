import os
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return redirect(url_for('static', filename='Index.html'))

@app.route('occs home.html')
def assignment_1():
    return redirect(url_for('static', filename='occs home.html'))
@app.route('')
def assignment_3():
    return redirect(url_for('static', filename=''))

@app.route('')
def assignment4():
    return redirect(url_for('static', filename=''))
@app.route('')
def assignment5():
    return redirect(url_for('static', filename=''))
@app.route('')
def assignment6():
    return redirect(url_for('static', filename=''))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
