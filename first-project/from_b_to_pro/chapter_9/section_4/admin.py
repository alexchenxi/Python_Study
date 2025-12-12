from user import User


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def showPrivileges(self):
        print(f"Admin role has following previliges:")
        for p in self.privileges:
            print(f"- {p}")


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()
