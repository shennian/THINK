def is_new_user(db, username):
    num = db.find({"username": username}).count()
    if num != 0:
        return False
    return True