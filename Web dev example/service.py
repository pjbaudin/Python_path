'''
Quick web api
'''

# Import library
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

app.run(debug=True)
    