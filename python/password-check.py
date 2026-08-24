import string

def check_common_pass(password):
    with open('100k-most-used-passwords-NCSC.txt', 'r') as f:
        common = f.read().splitlines()
    if password in common:
        return True
    return False

def strength_check(password):
    score = 0
    length = len(password)

    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    charicters = [uppercase, lowercase, digit, special]

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if length >= 20:
        score += 1

    score += sum(charicters) - 1

    if score < 4: 
        return "Weak.", score
    elif score == 4:
        return "Ok.", score
    elif 4 < score < 6:
        return "Good.", score
    else:
        return "Strong.", score

def feedback(password):
    if check_common_pass(password):
        return "The password is found in a common password lists. Please choose a different password. Score: 0/7"

    strength, score = strength_check(password)

    feedback = f"Password strength: {strength} (Score: {score}/7)\n"

    if score <= 4:
        feedback += "Suggestions to improve your password:\n"
        if len(password) <= 8:
            feedback += "- Make your password longer. 8 characters should be the minimum and 16 is recommended.\n"
        if not any(c.isupper() for c in password):
            feedback += "- Include uppercase letters.\n"
        if not any(c.islower() for c in password):
            feedback += "- Include lowercase letters.\n"
        if not any(c in string.punctuation for c in password):
            feedback += "- Add special characters (e.g., @, #, $).\n"
        if not any(c.isdigit() for c in password):
            feedback += "- Add numbers.\n"

    return feedback

password = input("Enter the password: ")
print(feedback(password))
