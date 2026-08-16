from flask import Blueprint, render_template, redirect, request, url_for, session, flash



skill_bp = Blueprint('about', __name__)


@skill_bp.route('/about')
def skill():
    return render_template('skill.html')