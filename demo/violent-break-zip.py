# 暴力破解压缩文件

import zipfile
import threading


def extract_file(z_file, password):
    """
    破解方法
    :param z_file: 需要破解的文件
    :param password: 尝试密码
    :return:
    """
    try:
        z_file.extractall(pwd = password)
        print("fonud password", password)
        event.set()
        return password
    except Exception as result:
        event.wait()
        print("未知错误 %s" % result)


def main():
    """
    主函数
    :return:
    """
    z_file = zipfile.ZipFile("python.zip")
    pass_file = open('pwd.txt')
    for line in pass_file.readlines():
        if event.isSet():
            print("end")
            return
        else:
            pwd = line.strip("\n")
            t = threading.Thread(target=extract_file, args=(z_file, pwd))
            t.start()


if __name__ == "__main__":
    event = threading.Event()
    main()
