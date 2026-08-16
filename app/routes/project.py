from flask import Blueprint, render_template, redirect, request, url_for, session, flash



project_bp = Blueprint('about', __name__)


@project_bp.route('/about')
def project():
    return render_template('project.html')