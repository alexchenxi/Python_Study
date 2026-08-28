from pathlib import Path

base_dir = Path(__file__).parent

file_name = input("请输入需要备份的文件名：")

index = file_name.rfind(".")
if index > 0:
    postfix = file_name[index:]
    copy_name = file_name[:index] + "[copy]" + file_name[index:]
    # 3. 备份文件写入数据
    with (
        open(base_dir / file_name, "rb") as old,
        open(base_dir / copy_name, "wb") as new,
    ):
        while True:
            content = old.read(1024)
            if len(content) == 0:
                break

            new.write(content)
    print(f"文件{file_name}拷贝完毕！")
else:
    print("输入的文件名称格式有误！")
