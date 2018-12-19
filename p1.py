li = ["北京", "上海", "南京", "无锡", "南通", "深圳", "广州", "徐州", "淮安", "连云港"]
file = open("role/hello.txt", "r", encoding="UTF-8")
for i in range(10):
    file_copy = open('role/hello'+li[i]+'.txt', "w", encoding="UTF-8")
    info = file.readlines()
    for line in info:
        line_new = line.replace("{城市}", li[i])
        file_copy.write(line_new)
        file_copy.close()
        file.seek(0, 0)

file.close()


