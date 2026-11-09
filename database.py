import mysql.connector
import pymysql.cursors

class Database():
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cursorclass = pymysql.cursors.DictCursor
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password,)

        def insert_classes(self, place1, place2):
            cursor = self.connection.cursor()
            sql = 'insert into classes(class_name, places) values (%s, %s)'
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (place1, place2,))
                self.connection.commit()

