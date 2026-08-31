class Student:
    def __init__(self, name="路人甲", id=1):
        """
        :param id
        :param name
        """
        self.name = name
        self.id = id

    def __str__(self):
        """
        打印对象时自动调用，return字符串
        """
        return f"This student name is {self.name}, his/her Id is {self.id:04d}!"

    def show_info(self):
        print(f"This student name is {self.name}, his/her Id is {self.id:04d}!")


s1 = Student(name="Jack", id=22)
s2 = Student()
print(s1)

# s1.show_info()
# s2.show_info()
