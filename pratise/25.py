# python编码处理及加密解密
import chardet
import sys

s = "肯定"
print(type(s))

s1 = s.encode("utf-8")
print(s1, chardet.detect(s1))


s2 = s.encode("gbk")
print(s2, chardet.detect(s2))

print(sys.getdefaultencoding())
