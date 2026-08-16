from flask import Flask





def create_app():
    app = Flask(__name__)


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