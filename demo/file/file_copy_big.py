# 复制文件（针对大文件）

# 1、打开文件
file_read = open("hello.txt", "r", encoding="UTF-8")
file_write = open("hello1.txt", "w", encoding="GBK")

# 2、读、写
while True:
    t_read = file_read.readline()
    if not t_read:
        break
    file_write.writelines(t_read)

# 3、关闭文件
file_read.close()
file_write.close()
