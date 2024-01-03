import mysql.connector

db = mysql.connector.connect(
    
    host= 'localhost',
    user = 'root',
    passwd = 'password123',
    database = 'chat',
    
)

cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS chat')

print('Created database')