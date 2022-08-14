import json

class User:
    def __init__(self, id, uname, passw, email):
        self.id = id
        self.uname = uname
        self.passw = passw
        self.email = email

def update_user_db(users):
    encoded_users = []
    for user in users:
        encoded_users.append([user.id, user.uname, user.passw, user.email])
    open("user_db.txt", "w").write(json.dumps(encoded_users))

def load_user_db():
    users = open("user_db.txt", "r").read()
    decoded_users = []
    for user in json.loads(users):
        decoded_users.append(User(id=user[0], uname=user[1], passw=user[2], email=user[3]))
    return decoded_users