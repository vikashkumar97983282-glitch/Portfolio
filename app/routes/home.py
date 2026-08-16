from flask import Blueprint, redirect, render_template, url_for, session, flash


home_bp = Blueprint('home', __name__)



@home_bp.route('/')
def home():
    return render_template('home.html')