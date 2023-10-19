from flask import Flask , render_template, render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/sign_up')
def sign_up():
    return render_template("signup.html")

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)