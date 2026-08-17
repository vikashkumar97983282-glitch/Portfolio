from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os


mail = Mail()

# Load the project's .env file before reading its settings.
load_dotenv()


def create_app():
    app = Flask(__name__)


    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-secret-key")

    # Email configuration
    app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT", "587"))
    app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS", "true").lower() == "true"
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_USERNAME")

    mail.init_app(app)


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
