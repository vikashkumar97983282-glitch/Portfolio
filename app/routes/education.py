from flask import Blueprint, render_template, redirect, request, session, url_for, flash



education_bp = Blueprint('education', __name__)



@education_bp.route('/education')
def education():
    return render_template('education.html')