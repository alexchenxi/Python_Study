class Phone:
    def __del__(self):
        print(
            f"Phone {self.brand} {self.model} recycled, return you ${self.value * 0.6:.2f}."
        )

    def __init__(self, brand, model, value):
        self.brand = brand
        self.model = model
        self.value = value


p1 = Phone("IPhone", "17", 6999)
