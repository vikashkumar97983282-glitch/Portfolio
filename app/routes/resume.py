from flask import Blueprint, render_template, redirect, request, url_for, session, flash



resume_bp = Blueprint('about', __name__)


@resume_bp.route('/about')
def resume():
    return render_template('resume.html')