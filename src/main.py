if __name__ == "__main__":
    index = 0;
    menu = "Register,Login".split(",")
    logged_in_menu = ""
    print("Menu\nSelect a menu option")
    for m in menu:
        index = index + 1
        print(f"{index}. {m}")
