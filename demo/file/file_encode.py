# 文件编码，ASCII编码和UNICODE编码
# 在ASCII码中，一个ASCII码占用1个字节，最大256个字符
# Unicode使用1-6个字节描述一个UTF-8字符，大多数汉字用三个字节表示
# python  默认使用ASCII编码，python 3 默认使用UTF-8编码

# 在引号前面的u告诉解析器这是一个utf-8编码格式的字符串
# python 3能正确输出，python 2则无法正确输入出中文
hello_str = u"hello你好"

for c in hello_str:
    print(c)
