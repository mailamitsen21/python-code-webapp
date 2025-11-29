from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Hi this is API test from Amit@Sen"
