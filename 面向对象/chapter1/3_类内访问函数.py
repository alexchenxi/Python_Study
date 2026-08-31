class Car:
    def run(self):
        print(f"Car NO.{id(self)} can run!")

    def work(self):
        self.run()


c1 = Car()
c1.work()
