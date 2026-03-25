from flask import Blueprint, jsonify
from services.registrar_service import get_registrar_dashboard, manage_enrollments, generate_reports

registrar_bp = Blueprint('registrar', __name__)

@registrar_bp.route('/dashboard')
def dashboard():
    return jsonify(get_registrar_dashboard())

@registrar_bp.route('/enrollments')
def enrollments():
    return jsonify(manage_enrollments())

@registrar_bp.route('/reports')
def reports():
    return jsonify(generate_reports())