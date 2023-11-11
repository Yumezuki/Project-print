from flask import Flask , render_template, render_template

app = Flask(__name__)

# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/sign_up')
# def sign_up():
#     return render_template("signup.html")

@app.route('/main_page')
def main_page():
    return render_template("main_page.html")


@app.route('/search')
def search():
    return render_template("search_page.html")

@app.route('/notifications')
def noti():
    return render_template("noti_have.html")

@app.route('/myprofile')
def profile():
    return render_template("pofile.html")


if __name__ == "__main__":
    app.run(debug=True)
