import sql_manager

def verify_password(password,username):
    hasCapitals = True in map(lambda l:l.isupper(),password)
    pass_not_in_username = password not in username
    if len(password) > 8 and hasCapitals and pass_not_in_username:
        return True
    return False

def verify_username(username):
    if username not in sql_manager.get_all_usernames():
        return True
    return False

