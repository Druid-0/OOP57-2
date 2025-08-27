


def require_admin(func):
    def wrapper(user):
        if user == "admin":
            func(user)
        else:
            print("denied")
    return wrapper


@require_admin
def delete_database(user):
    print("Database deleted!")

delete_database("admin")  # вывд: Database deleted!
delete_database("user1")  # вывод: Access denied