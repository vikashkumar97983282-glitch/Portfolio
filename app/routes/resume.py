from flask import Blueprint, render_template, redirect, request, url_for, session, flash



resume_bp = Blueprint('resume', __name__)


@resume_bp.route('/resume')
def resume():
    return render_template('resume.html')