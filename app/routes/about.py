from flask import Blueprint, render_template, redirect, request, url_for, session, flash



about_bp = Blueprint('about', __name__)


@about_bp.route('/about')
def about():
    return render_template('about.html')