import pymysql
from structure_exersise.config import ReadConfig
def get_db_con():
    con=pymysql.connect(host=ReadConfig.host,
                        port=ReadConfig.port,
                        user=ReadConfig.user,
                        password=ReadConfig.password,
                        db=ReadConfig.database)
    return con

'''查询功能'''
def query_db(sql):
    con=get_db_con()
    cursor=con.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    cursor.close()
    return data




