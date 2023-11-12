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

@views.route('/profile')
def profile():
    return render_template("profile.html")

@views.route('/noti')
def noti_have():
    return render_template("noti_have.html")

@views.route('/details')
def detail():
    return render_template("Detail.html")