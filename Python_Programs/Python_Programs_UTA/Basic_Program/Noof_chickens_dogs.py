"""
he first integer is the number of heads and the second integer is the number of legs of all the creatures in a farm which consists of chickens and dogs. Your function should calculate and return the number of chickens and number of dogs in the farm in a list as specified below. If it is impossible to determine the correct number of chickens and dogs with the given information then your function should return None. Example 1, if your function received the following numbers:

5, 12 
This means that someone has counted a total of 5 heads and total of 12 legs in the farm. Now, your function should calculate how many chickens and how many dogs are in the farm and return that information in a list exactly as shown below.
[4, 1] 
this means that there were 4 chickens and 1 dog in the farm.

Example 2, if your function received the following numbers:
7, 12 
Then it should return:
None

"""

def howmany(heads,legs):
    
    chicken_heads = heads
    dog_heads = 1
    list = [0,0]
    if(chicken_heads * 2 > legs):     # 2 legs for chicken
        return "None"
    else:
            
        
        while(chicken_heads >= 0):
            for dog_heads in range(0, heads+1):
                sum = chicken_heads * 2 + dog_heads * 4
                if(sum == legs):
                    list[0] = chicken_heads
                    list[1] = dog_heads
                    return list
            chicken_heads = chicken_heads - 1       

    if(sum != legs):
        
     return "None"
            

     
print(howmany(10,26))                  
            
        
