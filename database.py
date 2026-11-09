import mysql.connector
import pymysql.connection

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='college2db',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()
sql = 'SELECT * from teachers'
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)