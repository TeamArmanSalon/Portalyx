from flask import Blueprint, jsonify
from services.faculty_service import get_faculty_dashboard, get_classes, grade_students

faculty_bp = Blueprint('faculty', __name__)

@faculty_bp.route('/dashboard')
def dashboard():
    return jsonify(get_faculty_dashboard())

@faculty_bp.route('/classes')
def classes():
    return jsonify(get_classes())

@faculty_bp.route('/grade')
def grade():
    return jsonify(grade_students())