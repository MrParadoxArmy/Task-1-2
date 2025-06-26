import re

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., !, @, #).")

    # Strength rating
    if score == 5:
        return "Strong", feedback
    elif score >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback

# Example usage
password = input("Enter a password: ")
strength, feedback = analyze_password(password)
print(f"Strength: {strength}")
if feedback:
    print("Suggestions:", ", ".join(feedback))