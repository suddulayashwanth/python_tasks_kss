is_logged_in = True


def login_required(function):
    def wrapper():
        if is_logged_in:
            function()
        else:
            print("Access denied. Please log in.")

    return wrapper


@login_required
def view_profile():
    print("Welcome! You can view your profile.")


view_profile()