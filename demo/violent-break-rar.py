import os
import sys
import zipfile

try:
    from unrar import rarfile
except Exception as result:
    path = "" + os.path.dirname(sys.executable) + '\\script\\pip" insatll --upgrade pip'
    os.system(path)
    path = "" + os.path.dirname(sys.executable) + '\\script\\pip" install unrar'
    os.system(path)
    from unrar import rarfile


def decryptRarZipFile(filename):
    if filename.endwith(".zip"):
        fp = zipfile.ZipFile(filename)
    elif filename.endwith(".rar"):
        fp = rarfile.RarFile(filename)

    desPath = filename[:-4]
    if not os.path.exists(desPath):
        os.mkdir(desPath)
    try:
        fp.extractall(desPath)
        fp.close()
        print("no password")
        return
    except Exception as result:
        try:
            fpPwd = open("pwd.txt")
        except:
            print("当前目录找不到字典")
            return
        for pwd in fpPwd:
            pwd = pwd.strip("\n")
            try:
                if filename.endwith(".zip"):
                    for file in fp.namelist():
                        fp.extract(file, path=desPath, pwd=pwd.encode())
                        os.rename(desPath + "\\" + file, desPath + "\\" + file.encode("cp437").decode("gbk"))
                    print("success====>", pwd)
                    fp.close()
                    break
                elif filename.endwith(".rar"):
                    fp.extractall(path=desPath, pwd=pwd)
                    print("success===>", pwd)
                    fp.close()
                    break
            except:
                pass
        fpPwd.close()


if __name__ == "__main__":
    filename = sys.argv[1]
    if os.path.isfile(filename) and filename.endwith((".zip", ".rar")):
        decryptRarZipFile(filename)
    else:
        print('必须是rar或zip文件')
