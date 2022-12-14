"""
数据库操作类
类名：Database
方法：
    init:
        conn
        cursor
    read
    write
    del:
        cursor.close()
        conn.close()
"""
import pymysql


class Database:
    def __init__(self, database, host='localhost',
                 port=3306, user='root', password='root',
                 cursor=pymysql.cursors.Cursor):
        self.conn = pymysql.connect(host=host, port=port,
                                    user=user, password=password,
                                    database=database, charset='utf8')
        self.cursor = self.conn.cursor(cursor=cursor)
        self.cursor_type = () if cursor == pymysql.cursors.Cursor else []

    def read(self, sql, args=None):
        """读操作"""
        try:
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            print(e)
            return 0, self.cursor_type
        else:
            all_data = self.cursor.fetchall()
            return rows, all_data

    def write(self, sql, args=None):
        """写操作"""
        try:
            rows = self.cursor.execute(sql, args)
        except Exception as e:
            print(e)
            self.conn.rollback()
            return 0
        else:
            self.conn.commit()
            return rows

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = Database('advanced')
    # database.read()  # rows data
    # rows, data = db.read('select * from news where itle=%s', ['title1'])

    # 删除操作
    print(db.write('delete from new where title = %s', ['title4']))
