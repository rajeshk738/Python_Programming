"""
Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

"""

while(True):
    N = int(input())
    if(N>=2):
        break;

input_list = []
result = []


for i in range(N):
    person = str(input())
    score = float(input())
    input_list.append([person,score])

input_list.sort(key = lambda x: x[1])

val = input_list[0][1]

for i in range(1,N):
    
    if(val == input_list[i][1]):
        continue
    
    val2 = input_list[i][1]
    result.append(input_list[i][0])
    
    for i in range(i+1,N):

        if val2 == input_list[i][1]:
            result.append(input_list[i][0])
            
    break


result.sort()

for i in range(0,len(result)):
    print(result[i])


