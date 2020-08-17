# pip install mysql-connector

import mysql.connector as m

print('Connecting MySQL database...')

mydb = m.connect(host="localhost",user="root",password="root")

print('\nDatabase Connected\n')

mycursor = mydb.cursor()

print('\nExecuting Query\n')
mycursor.execute("show databases")  # data stored in mycursor


for i in mycursor:
    print(i)


print('\nDone')    
