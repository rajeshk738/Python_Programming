# convert celsius to Fahrenheit
celsius = float(input("Enter the celsius temperature"))

fahrenheit = ((celsius * 9) / 5) + 32
print(fahrenheit)
if fahrenheit<32 :
    print("It is freezing")
elif fahrenheit<50 :
    print("It is chilly")
elif fahrenheit<90:
    print("It is ok")
else :
    print("It is hot")
