class HuaweiMate60:
    def performance(self):
        return 60


class HuaweiMate80(HuaweiMate60):
    def performance(self):
        return 80


class Iphone:
    def performance(self):
        return 70


def object_play(guochan: HuaweiMate60, jinkou: Iphone):
    print("*" * 17 + "Compare Model" + "*" * 14)
    if guochan.performance() > jinkou.performance():
        print("Huawei wins!")
    else:
        print("Iphone wins!")


if __name__ == "__main__":
    h1 = HuaweiMate60()
    h2 = HuaweiMate80()
    i1 = Iphone()
    object_play(h1, i1)
    object_play(h2, i1)
    object_play(h1, h2)

"""
多态的好处
1. 在不改变代码框架的情况下，通过多态可以实现模块和模块之间的解耦合，实现了软件系统的可拓展
解耦合：职责拆分，明确接口，各干各的。改 A 尽量不影响 B，部件可以单独拿出来复用。
2. 多态相当于：父类框架，不做任何修改的情况下，可以可拓展的使用后来人写的东西
3. 抽象类 抽象接口

抽象类（接口）
父类确定有哪些方法（父类制定接口标准）
子类来实现具体的方法（子类实现接口标准）

抽象类:含有抽象方法的类
抽象方法：方法体是空实现pass的方法 
"""
