# f=open("./file.txt",'r',encoding='utf-8')
with open("./file.txt", 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)
# f.close()
