from flask import Flask,render_template
app  = Flask(__name__)

@app.route("/new2")
def any1():
    name = "pk"
    return render_template('index.html',name = name)

@app.route("/about")
def any2():
    name = "parth"
    return render_template('about.html',name = name)

@app.route("/self")
def any3():
    name = "mark"
    return render_template("about.html",name = name)

@app.route("/new")
def fun2():
    return "hello world"
    


app.run(debug = True)