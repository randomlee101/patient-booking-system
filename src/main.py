from src.view import UserView
from src.models import UserList

if __name__ == "__main__":
    while True:
        if UserList.currentUser is None:
            UserView.user_menu()
        else:
            UserView.logged_in_menu()

