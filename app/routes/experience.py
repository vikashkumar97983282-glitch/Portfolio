from flask import Blueprint, render_template, request, redirect, url_for, session, flash




experience_bp = Blueprint('experience', __name__)



@experience_bp.route('/experience')
def experience():
    return render_template('experience.html')