import pymysql
import pandas as pd

def cases():
    conn = pymysql.connect(
        host = '*********',  #数据库的主机名
        port = ****,  #数据库的端口号
        user = '****',  #数据库的用户名
        password = '*********',  #数据库的密码
        charset='****',  #数据库的编码方式
        cursorclass=pymysql.cursors.DictCursor
    )

    conn.select_db('********')  #选定您需要的数据库
    cursor = conn.cursor()
    SQL = 'SELECT * FROM ******'  #选择您需要的数据表和数据
    cursor.execute(SQL)
    result = cursor.fetchall()

    df = pd.DataFrame(result)
    return df