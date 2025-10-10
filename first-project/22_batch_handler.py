gpa_dict = {"Alex": 3.945, "Bob": 3.21, "Chris": 2.95}
for name, gpa in gpa_dict.items():
    # f""就像是javascript es6里的模板字符串`${variable}`
    print(f"Hello {name}, your score is {round(gpa, 2)}")  # this one is best
    print("Hello {0}, your score is {1:.2f}".format(name, gpa))
    # 注意要给形参赋值实参
    print("""Hello {name}, your score is {gpa:.2f}""".format(name=name, gpa=gpa))
