def get_dashboard():
    return {
        "message": "Student dashboard data (mock)",
        "subjects": ["Math", "Science", "English"]
    }

def get_profile(student_id=None):
    return {
        "id": student_id or 1,
        "name": "John Doe",
        "email": "john@example.com"
    }