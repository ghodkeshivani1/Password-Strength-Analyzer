import string
import secrets

def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9).")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters such as @, #, or !.")

    common_passwords = {
        "password", "password123", "12345678",
        "qwerty123", "admin123"
    }

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords.")

    if password.lower() in common_passwords or len(password) < 8:
        strength = "Weak"
    elif score <= 3:
        strength = "Medium"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, suggestions


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(
            secrets.choice(characters) for _ in range(length)
        )

        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password


def main():
    print("=" * 40)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    password = input("Enter a sample password to analyze: ")

    strength, suggestions = analyze_password(password)

    print("\nPassword Strength:", strength)
    print("Password Length:", len(password), "characters")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nYour password meets all the basic checks!")

    print("\nSuggested Strong Password:", generate_password())


if __name__ == "__main__":
    main()
```
