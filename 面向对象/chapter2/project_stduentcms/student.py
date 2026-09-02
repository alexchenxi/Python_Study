class Student:
    def __init__(self, name: str, gender: str, age: int, phone: str, desc: str):
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        name, age, gender, phone, desc = self.__dict__.values()
        return f"学生姓名：{name}；年龄：{age}；性别：{gender}；手机号码：{phone}；个人信息：{desc}"


if __name__ == "__main__":
    s = Student("张三", "男", 18, "13800000000", "一个好学生")
    print(s)
