from flask import Flask , render_template, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
@app.route('/login')
def login():
    login = bool(request.cookies.get('login'))
    if login:
        return '0'
    else:
        return render_template('login.html')

@app.route('/sign_up')
def sign_up():
    return render_template("signup.html")

@app.route('/main_page')
def main_page():
    return render_template("main_page.html")


@app.route('/search')
def search():
    return render_template("search_page.html")

@app.route('/notifications')
def noti():
    return render_template("noti_have.html")

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/')
# def index():
#     users = Places.query.all()
#     place = [{'id': user.id, 'name': user.name, 'description': user.description,
#                    'location': user.location, 'recommend_name': user.recommend_name,
#                    'recommend_image': user.recommend_image, 'recommend_detail': user.recommend_detail}
#                   for user in users]
#     print(place)
#     return render_template('index.html', places=place)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Places(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False, nullable=False)
#     image = db.Column(db.String(80), unique=False, nullable=False)
#     description = db.Column(db.String(80), unique=False, nullable=False)
#     location = db.Column(db.String(80), unique=False, nullable=False)
#     recommend_name = db.Column(db.String(80), unique=False, nullable=False)
#     recommend_image = db.Column(db.String(80), unique=False, nullable=False)
#     recommend_detail = db.Column(db.String(80), unique=False, nullable=False)
# @app.get('/places')
# def create():
#     # Create Data
#     create_user = Places(
#         name='adg',
#         image='https://media.discordapp.net/attachments/1127984088532398241/1164047165816049737/IMG_20231006_144844.jpg?ex=655d79e7&is=654b04e7&hm=b03dc6425405812420d270917cd5190a30ca32c142f32347ee4af650f9bcf9e7&=&width=496&height=662',
#         description='adsga',
#         location='asdgasgd',
#         recommend_name='asdg',
#         recommend_image='adgasdg',
#         recommend_detail='adgadgs'
#     )
#     db.session.add(create_user)
#     db.session.commit()
#     return jsonify([])