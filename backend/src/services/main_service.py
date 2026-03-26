def format_response(data, status=200):
    return {"status": status, "data": data}

def validate_required_fields(data, fields):
    missing = [f for f in fields if f not in data or data[f] is None]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    return True, ""