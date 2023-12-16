from src.models import UserModel, UserList


class UserController:

    @staticmethod
    def register():
        users_count = UserList.countUsers()
        user = UserModel(users_count + 1, "randomlee", "randomlee", role="patient")
        user.register()
        return "Account Created Successfully"
