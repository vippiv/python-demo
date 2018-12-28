# 实现转换图片上的文字
# 需要安装插件，按以下步骤
# 1、https://www.cnblogs.com/jianqingwang/p/6978724.html
# 2、https://blog.csdn.net/qiushi_1990/article/details/78041375
# 软件包下载地址：http://www.bkill.com/download/171436.html
from PIL import Image
import pytesseract
text = pytesseract.image_to_string(Image.open('D:/python-demo/assets/poem-chunxue.jpg'), lang='chi_sim')
print(text)
