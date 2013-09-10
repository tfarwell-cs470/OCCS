import os
from flask import Flask, redirect, url_for

app = Flask(__name__)


# Home page. Index link for all assignments
@app.route('/')
def hello():
    return redirect(url_for('static', filename='Index.html'))
# # Local: 470 Site

# @app.route('/local')
# def local():
#     return redirect(url_for('static', filename='occs home.html'))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)