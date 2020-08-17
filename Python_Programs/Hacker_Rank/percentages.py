"""
You have a record of  students. Each record contains the student's name, and 
their percent marks in Maths, Physics and Chemistry. The marks can be floating values. 
The user enters some integer  followed by the names and marks for  students. 
You are required to save the record in a dictionary data type. The user then enters a student's name. 
Output the average percentage marks obtained by that student, correct to two decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0

56.00

"""
students = {}

while True:
    N = int(input())
    
    if N >= 2 and N <= 100:
        for i in range(N):
            name,maths,physics,chemistry = input().split()
            maths = float(maths)
            physics = float(physics)
            chemistry = float(chemistry)
            
            students[name]= [maths,physics,chemistry]
        
        break

result_person = str(input())
result_list = students[result_person]

Average = sum(result_list) / len(result_list)  
Average = round(Average,2)
print("{0:.2f}".format(Average))      

