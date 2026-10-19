# Password strength checker
import string
def check_password_strength(password: str) -> dict[str, object]:
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    checks = {
        "at least 12 characters": len(password) >= 12,
        "lowercase letter": any(char.islower() for char in password),
        "uppercase letter": any(char.isupper() for char in password),
        "number": any(char.isdigit() for char in password),
        "symbol": any(char in string.punctuation for char in password),
    }

    score = sum(checks.values())
    strength = "weak" if score < 3 else "fair" if score < 5 else "strong"

    return {
        "strength": strength,
        "score": score,
        "feedback": [name for name, passed in checks.items() if not passed],
    }
```

