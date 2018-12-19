# 复制文件（针对小文件）

# 1、打开文件
file_read = open("hello.txt", "r", encoding="UTF-8")
file_write = open("hello1.txt", "w", encoding="GBK")

# 2、读、写
t_read = file_read.read()
file_write.write(t_read)

# 3、关闭文件
file_read.close()
file_write.close()
