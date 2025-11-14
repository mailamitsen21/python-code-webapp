import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Azure! Flask on Python 3.11."

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
