# 批量检测url的有效性（批量检测url是否可访问）
import urllib.request
import time


def check_url_validity(entry, right_out_file):
    """
    批量检测url有效性并将正确的url存放到另一个文本文件中
    :param entry: url列表文件
    :param right_out_file: 正确的url输出文件
    :return:
    """
    opener = urllib.request.build_opener()
    # 设置用户代理，防止被封
    opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
    file = open(entry, 'r', encoding="UTF-8")
    # 打开输出文件，没有则自动创建
    output_file = open(right_out_file, "w+", encoding="UTF-8")
    lines = file.readlines()
    url_list = []
    for line in lines:
        temp = line.replace('\n', '')
        url_list.append(temp)

    print('开始检查：')
    for url in url_list:
        temp_url = url
        try:
            opener.open(temp_url)
            print(temp_url + ' 没问题')
            output_file.write(temp_url + "\n")
        except urllib.error.HTTPError:
            print(temp_url + ' 访问页面出错')
            time.sleep(2)
        except urllib.error.URLError:
            print(temp_url + ' 访问页面出错')
            time.sleep(2)
        except Exception as result:
            print(result)


check_url_validity("D:/python-demo/urls.txt", "D:/python-demo/right_url.txt")
