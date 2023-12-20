from src.models import UserModel, UserList


class UserController:

    @staticmethod
    def register(username, password, role):
        users_count = UserList.countUsers()
        user = UserModel(users_count + 1, username, password, role)
        user.register()
        return "Account Created Successfully\n"

    @staticmethod
    def login(username, password):
        user = UserModel.login(username, password)
        if type(user) is not UserModel:
            return user + "\n"
        return "Logged in as " + user.__str__() + "\n"

    @staticmethod
    def logout():
        UserList.currentUser = None
        print("Signed Out Successfully\n")
