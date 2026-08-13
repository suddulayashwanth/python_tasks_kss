import pandas as pd

roles = {"Yash": "admin", "Rahul": "user", "Priya": "guest"}

role_series = pd.Series(roles)


def access_control(function):
    def wrapper(username):
        user_role = role_series.get(username)

        if user_role == "admin":
            return function(username)
        else:
            print(username, "does not have permission")

    return wrapper


@access_control
def view_report(username):
    print(username, "is viewing the report")


@access_control
def delete_record(username):
    print(username, "deleted a record")


view_report("Yash")

delete_record("Rahul")