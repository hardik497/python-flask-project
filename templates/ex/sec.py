from flask import Flask
app = Flask(__name__)

@app.route("/new")
def hello():
    return "hello everyone"
app.run(debug=True)