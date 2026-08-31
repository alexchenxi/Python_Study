class Student:
    def __init__(self, weight=100, name="xiaoming"):
        self.weight = weight
        self.name = name

    def work_out(self):
        print(f"{self.name} is working out...")
        self.weight -= 0.5

    def feast(self):
        print(f"{self.name} is having feast...")
        self.weight += 2

    def __str__(self):
        return f"Student {self.name}'s current weight is {self.weight}kg."


if __name__ == "__main__":
    # 只有直接运行本文件的时候，才执行这块里面的代码；被别人导入的时候，这块代码不跑。
    xm = Student()
    print(xm)
    xm.work_out()
    print(xm)
    xm.feast()
    print(xm)
