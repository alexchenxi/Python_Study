class Father:
    def __init__(self):
        self.gender = "Male"

    def run(self):
        print(f"{self} can run!")


class Son(Father):
    pass
    # def __init__(self):
    #     super()


s = Son()
s.run()
