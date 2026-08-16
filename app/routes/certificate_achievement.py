from flask import Blueprint, render_template, redirect, request, session, url_for, flash




certi_bp = Blueprint('certi', __name__)


@certi_bp.route('/certi')
def certi():
    return render_template('certi.html')