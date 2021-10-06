from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def head():
    first = "This is my first condition experience in Flask Framework"
    return render_template("index.html",message = False)

@app.route("/first_path")
def mylist():
    names = ["Hans","Betty","Mirjam","Ruth"]
    return render_template("body.html",object = names)


if __name__=="__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0',port=80)