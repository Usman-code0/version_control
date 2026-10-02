def login(email, password):
    
    if not email or not password:
        return "Error: Email and password are required."

    
    if email == "admin@example.com" and password == "secure123":
        return f"Login successful. Welcome, {email}!"
    else:
        return "Login failed. Invalid credentials."


def logout(email):
    """Log out the current user."""
    return f"User {email} has been logged out."



result = login("admin@example.com", "secure123")
print(result)

result = login("user@example.com", "wrongpass")
print(result)

print(logout("admin@example.com"))
