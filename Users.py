
import json


class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password


class Users:

    def __init__(self):
        self.dict = []

    def add_new_user(self, email, password):

        with open("user.json") as file:
            self.dict = json.loads(file.read())
        with open("user.json", "w") as file:
            # self.dict[f"{new_user.last_id}"] = {"Username": new_user.email, "Password": new_user.password}
            new_user = User(email, password)
            self.dict.append({"name": new_user.email, "password": new_user.password})
            json.dump(self.dict, file,indent=6)
