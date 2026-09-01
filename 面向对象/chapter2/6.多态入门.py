"""
多态概述：
  专业：同一个函数，接受不同的参数，有不同的效果
  白话：同一个事物在不同时刻表现不同的形态

  条件：
    1.有继承
    2.有方法重写
    3.有父类引用指向子类对象
"""


class Animal:  # 抽象类（也叫：接口）
    def speak(self):  # 抽象方法
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Car:
    def speak(self):
        print("嘟嘟嘟")


def make_sound(animal: Animal):
    animal.speak()


if __name__ == "__main__":
    # an: Animal = Dog()  # 父类引用指向子类对象
    # d: Dog = Dog()  # 创建狗类对象
    d = Dog()
    c = Cat()

    make_sound(d)
    make_sound(c)
    car = Car()
    make_sound(car)
