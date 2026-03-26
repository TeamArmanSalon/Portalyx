from flask import Blueprint, jsonify
from services.student_service import get_dashboard, get_profile

student_bp = Blueprint('student', __name__)

@student_bp.route('/dashboard')
def dashboard():
    data = get_dashboard()
    return jsonify(data)

@student_bp.route('/profile')
def profile():
    data = get_profile()
    return jsonify(data)