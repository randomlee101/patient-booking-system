from src.controller import UserController
from src.models import UserModel, UserList


class UserView:

    @staticmethod
    def user_menu():
        index = 0
        menu = "Register,Login".split(",")
        print("Menu\nSelect a menu option")
        for m in menu:
            index = index + 1
            print(f"{index}. {m}")

        response = int(input("Enter the menu option: "))
        functions = [UserView.register, UserView.login]
        return functions[response - 1]()

    @staticmethod
    def logged_in_menu():
        index = 0
        menu = "Home,Appointments,Sign Out".split(",")
        print("Menu\nSelect a menu option")
        for m in menu:
            index = index + 1
            print(f"{index}. {m}")

        response = int(input("Enter the menu option: "))
        functions = [None, None, UserController.logout]
        return functions[response - 1]()

    @staticmethod
    def register():
        index = 0
        username = input("Enter Username: ")
        password = input("Enter password: ")
        roles_list = "patient,doctor,receptionist,admin".split(",")
        print("\nSelect a role")
        for r in roles_list:
            index = index + 1
            print(f"{index}. {r}")
        selected_role_index = int(input("Enter option: "))
        role = roles_list[selected_role_index - 1]
        print(UserController.register(username, password, role))
        print(UserList.viewAllUsers())

    @staticmethod
    def login():
        username = input("Enter Username: ")
        password = input("Enter password: ")
        print(UserController.login(username, password))

