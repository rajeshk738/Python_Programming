import time

name_person = input(" Enter your name : ")
print("\n welcome {} to the quiz! \n".format(name_person))

score = 0
def scoreplus():
    global score
    score = score + 1
    return score

def scoreminus():
    global score
    score = score - 1

def f1():
    time.sleep(0.5)
    print("1. What is your name? ")
    print("a. rajesh ")
    print("b. ramesh ")
    print("c. lokesh ")
    answer = str(input("Enter your option: "))
    time.sleep(0.5)
    if answer=='a' :
        print("CORRECT")
        scoreplus()
        f2()
    else :
        print(" Please try again ")
        scoreminus()
        f1()
    
    
def f2():
    time.sleep(1)
    print("1. What is your age? ")
    print("a. 20 ")
    print("b. 25 ")
    print("c. 29 ")
    answer = str(input("Enter your option: "))
    time.sleep(0.5)
    if answer=='b' :
        print("CORRECT")
        scoreplus()
        f3()
    else :
        print(" Please try again ")
        scoreminus()
        f2()
           
    

def f3():
    time.sleep(1)
    print("1. What is your hobby? ")
    print("a. playing cricket ")
    print("b. listeneing music ")
    print("c. reading book ")
    answer = str(input("Enter your option: "))
    time.sleep(0.5)
    if answer=='b' :
        print("CORRECT")
        scoreplus()
        f4()
    else :
        print(" Please try again ")
        scoreminus()
        f3()
    

def f4():
    time.sleep(1)
    print("1. What is your college name? ")
    print("a. Andhra University ")
    print("b. Gitam university ")
    print("c. JNTU ")
    answer = str(input("Enter your option: "))
    time.sleep(0.5)
    if answer=='a' :
        print("CORRECT")
        scoreplus()
        f5()
    else :
        print(" Please try again ")
        scoreminus()
        f4()
    

def f5():
    time.sleep(1)
    print("1. What is your CGPA? ")
    print("a. 7.9 ")
    print("b. 7.6 ")
    print("c. 7.4 ")
    answer = str(input("Enter your option: "))
    time.sleep(0.5)
    if answer=='c' :
        print("CORRECT")
        scoreplus()
    else :
        print(" Please try again ")
        scoreminus()
        f5()
        
    print("\n\n Thank You for answering the Quiz\n")

    print("\n Your result is processing, please wait...")
    time.sleep(5)
    print("\n Your result is : ",score)

f1()



