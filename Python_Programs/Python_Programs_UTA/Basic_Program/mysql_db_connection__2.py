# pip install mysql-connector

import mysql.connector as m

print('Connecting MySQL database...')

mydb = m.connect(host="localhost",user="root",password="root",database='rajesh')

print('\nDatabase Connected\n')

mycursor = mydb.cursor()

print('\nExecuting Query\n')
mycursor.execute("select * from students")  # data stored in mycursor

result = mycursor.fetchall() #returns all records data

#result = mycursor.fetchone()  #fetches one record data

for i in result:
    print(i)


print('\nDone')    
