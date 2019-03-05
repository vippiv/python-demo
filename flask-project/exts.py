import pymysql
import pymysql.cursors

db = pymysql.connect(host='localhost', user='root', password='', db='test', port=3306, charset='utf8')
