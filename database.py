import mysql.connector
import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='admin',
    database='college2db',
    cursorclass=pymysql.cursors.DictCursor,
)

data = ("red 404", 21)



cursor = connection.cursor()
sql = 'insert into college2db.clases(c_name,places) values(%s,%s)'
with connection.cursor() as cursor:
    cursor.execute(sql, data)
    connection.commit()
result = cursor.fetchnone()
#for row in result:
    #print(row)
cursor.close()
connection.close()
