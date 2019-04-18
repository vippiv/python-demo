# _*_ coding:utf-8 _*_
# 1、打开文件
file = open("hello.txt", encoding='UTF-8')

# 2、读取文件内容，第一次打开时，文件指针会指向文件的开始位置，
text = file.read()

# 2.1、read()结束后指针指向文件末尾，再次调用read()将读取不到任何内容
print(text)
print("读取到的内容长度 %d" % len(text))

print("-" * 100)

txt = file.read() # 这里读取不到任何内容，因为文件指针位于文件末尾
print(txt)
print("读取到的内容长度 %d" % len(txt))

# 3、关闭文件，如果忘记关闭文件，会造成系统消耗
file.close()
