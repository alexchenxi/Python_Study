class Phone:
    def open(self):
        print(f"{id(self)} is opening....")

    def shutdown(self):
        print(f"{id(self)} is shutting down....")

    def takePic(self):
        print("taking picture...")


p1 = Phone()
p1.takePic()
