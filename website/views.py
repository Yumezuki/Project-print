from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/main_page', methods=['GET', 'POST'])
@login_required
def main_page():
    return render_template("main_page.html", user=current_user)


@views.route('/noti')
def noti_have():
    return render_template("noti_have.html")


@views.route('/totticafe')
def totti():
    return render_template("detail_totticafe.html")

@views.route('/timbercafe')
def tim():
    return render_template("detail_timbercafe.html")

@views.route('/the_boon')
def theboon():
    return render_template("detail_the_boon.html")

@views.route('/swimming_pool')
def swim():
    return render_template("detail_swimming_pool.html")

@views.route('/sport_field')
def sport():
    return render_template("detail_sport_field.html")

@views.route('/saisaicafe')
def saisai():
    return render_template("detail_saisaicafe.html")

@views.route('/playlistcafe')
def playlist():
    return render_template("detail_playlistcafe.html")

@views.route('/paplerncafe')
def paplern():
    return render_template("detail_paplerncafe.html")

@views.route('/nommahalai')
def nommahalia():
    return render_template("detail_nommahalai.html")

@views.route('/mesmile')
def mesmile():
    return render_template("detail_mesmile.html")

@views.route('/mala')
def mala():
    return render_template("detail_mala.html")

@views.route('/luck&roll')
def luckroll():
    return render_template("detail_luck&roll.html")

@views.route('/lanprajom')
def lanprajom():
    return render_template("detail_lanprajom.html")

@views.route('/huatake_market')
def huatake():
    return render_template("detail_huatake_market.html")

@views.route('/fitness')
def fitness():
    return render_template("detail_fitness.html")

@views.route('/decisivecafe')
def deciviver():
    return render_template("detail_decisivecafe.html")

