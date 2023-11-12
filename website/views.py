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


