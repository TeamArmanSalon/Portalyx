from flask import Blueprint, jsonify
from services.admin_service import get_admin_dashboard, manage_users, get_reports

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
def dashboard():
    return jsonify(get_admin_dashboard())

@admin_bp.route('/users')
def users():
    return jsonify(manage_users())

@admin_bp.route('/reports')
def reports():
    return jsonify(get_reports())