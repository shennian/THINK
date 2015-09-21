from werkzeug.security import generate_password_hash, check_password_hash


def check_password(password, db_password):
    return check_password_hash(db_password, password)


def insert(database, username, password):
    data = {"username": username, "password": password}
    database.insert(data)


def get_password(db, username):
    data = db.find({"username": username})
    for i in data:
        return generate_password_hash(i["password"])


def is_new_user(db, username):
    num = db.find({"username": username}).count()
    if num != 0:
        return False
    return True
