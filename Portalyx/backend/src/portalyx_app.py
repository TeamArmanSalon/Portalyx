from flask import Flask
import os
from dotenv import load_dotenv

# Import routes
from routes.auth import auth_bp
from routes.student import student_bp
from routes.main import main_bp
from routes.admin import admin_bp
from routes.faculty import faculty_bp
from routes.registrar import registrar_bp

load_dotenv()

def create_portal():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY") or "your-secret-key-here"

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(student_bp, url_prefix='/api/student')
    app.register_blueprint(main_bp, url_prefix='/api/main')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(faculty_bp, url_prefix='/api/faculty')
    app.register_blueprint(registrar_bp, url_prefix='/api/registrar')

    return app

if __name__ == '__main__':
    portal = create_portal()
    portal.run(host='0.0.0.0', port=5555, debug=True)