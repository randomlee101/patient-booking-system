from src.controller import UserController
from src.models import UserModel, UserList


class UserView:

    @staticmethod
    def register():
        print(UserController.register())
        print(UserController.register())
        print(UserList.viewAllUsers())


if __name__ == "__main__":
    UserView.register()