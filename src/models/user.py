from datetime import datetime


class UserModel:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def login(username, password):
        return True

    def register(self):
        UserList.addUser(self)

    def updateProfile(self):
        pass

    def __str__(self):
        return f"{self.username} {self.role}"

    def __repr__(self):
        return f"{self.user_id} {self.username} {self.role}"


class UserList:
    users = []

    @staticmethod
    def addUser(user: UserModel):
        UserList.users.append(user)

    @staticmethod
    def countUsers():
        return len(UserList.users)

    @staticmethod
    def viewAllUsers():
        return UserList.users
