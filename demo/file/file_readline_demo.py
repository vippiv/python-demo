# readline方法一次只读取一行内容

file = open("hello.txt", "r", encoding="UTF-8")

while file:
    text = file.readline()  # 指针会自动移动到下一行
    # 判断是否读取到内容
    if not text:
        break

    print(text)


file.close()
