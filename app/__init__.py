from flask import Flask
from dotenv import load_dotenv
import os

# Load the project's .env file before reading its settings.
load_dotenv(override=True)


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-secret-key")
    app.config["RESEND_API_KEY"] = os.environ.get("RESEND_API_KEY")
    app.config["RESEND_FROM_EMAIL"] = os.environ.get("RESEND_FROM_EMAIL")
    app.config["RESEND_TO_EMAIL"] = os.environ.get("RESEND_TO_EMAIL")


    from app.routes import home_bp
    from app.routes import about_bp
    from app.routes import certi_bp
    from app.routes import contact_bp
    from app.routes import education_bp
    from app.routes import experience_bp
    from app.routes import project_bp
    from app.routes import resume_bp
    from app.routes import skill_bp


    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(certi_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(education_bp)
    app.register_blueprint(experience_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(skill_bp)


    return app
