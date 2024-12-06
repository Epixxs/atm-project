import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='',)
cursor = conn.cursor()
cursor.execute("create database ATM_MACHINE")
