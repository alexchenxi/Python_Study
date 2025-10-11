class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"Employee name: {self.name}, Employee Id: {self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_salary(self):
        return self.daily_salary * self.work_days


chen = FullTimeEmployee("Chen", "001", 35500)
li = PartTimeEmployee("Li", "002", 200, 20)
chen.print_info()
li.print_info()
print(chen.calculate_monthly_salary())
print(li.calculate_monthly_salary())
