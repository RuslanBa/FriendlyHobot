

def check_username(username):
    removed_chars = [' ', '@']
    chars = set(removed_chars)

    username_new = ''.join(filter(lambda x: x not in chars, username))
    return username_new
