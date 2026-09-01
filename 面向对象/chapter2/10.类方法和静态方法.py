class Student:
    school = "MIT"

    @classmethod
    def show1(cls):
        print(f"cls: {cls}")
        print(f"School: {cls.school}")

    @staticmethod
    def show2():
        print(f"show2")


if __name__ == "__main__":
    Student.show1()
    Student.show2()
