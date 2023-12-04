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
        pass

    def updateProfile(self):
        pass
