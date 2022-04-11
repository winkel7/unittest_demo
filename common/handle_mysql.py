import pymysql

from common.handle_conf import cof


class HandleMysql:
    def __init__(self):
        self.con = pymysql.connect(host=cof.get('mysql', 'host'),
                                   port=eval(cof.get('mysql', 'port')),
                                   user=cof.get('mysql', 'user'),
                                   password=cof.get('mysql', 'password'),
                                   charset=cof.get('mysql', 'charset'),
                                   cursorclass=pymysql.cursors.DictCursor) # 未指定cursorclass，则游标返回的是元组
        self.cur = self.con.cursor()

    def find_all(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.cur.close()
        return res

    def find_one(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        self.cur.close()
        return res

    def find_count(self, sql):
        res = self.cur.execute()
        self.cur.close()
        return res

    def __del__(self):
        self.con.close()


if __name__ == '__main__':
    res = HandleMysql().find_all('select * from futureloan.member where mobile_phone = "13265895752"')
    print(res)
