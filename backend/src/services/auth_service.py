def login_user(data):
    username = data.get("username")
    password = data.get("password")

    if username == "admin" and password == "1234":
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}, 401


def register_user(data):
    username = data.get("username")
    password = data.get("password")
    return {"message": f"User {username} registered (mock)"}