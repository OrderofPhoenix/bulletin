import re

# form validate

def is_username_valid(username):
    if len(username) > 20 or len(username) < 6:
        return False
    match_result = re.match(r'^\w+[-+.]?\w+', username, re.M| re.I)
    if match_result is None:
        return False
    else:
        str = ''
        group = match_result.group()
        for g in group:
            str += g
        if str == username:
            return True
        else:
            return False

def is_password_valid(password):
    if len(password) > 20 or len(password) < 6:
        return False
    else:
        return True

def is_email_valid(email):
    pass

def is_q_or_a_valid(q_or_a):
    if q_or_a == '':
        return False
    else:
        return True

