class Singleton:
    __instance = None
    name = "jack"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def show(self, n):
        print("------>show", Singleton.name, n)


s = Singleton()
s1 = Singleton()

print(s)
print(s1)
s.show(5)
s1.show(7)
