#program to convert seconds into days,hours,minutes, and seconds
no = int(input("Enter the a number to convert into days,hrs,min,sec "))
d = 24 * 60 * 60
h = 60 * 60
m = 60

days = no//d
hours = (no % d) // h
minutes =  ((no % d) % h) // m
seconds = (((no%d)%h)%m)

print(days," days ",hours," hours ",minutes," minutes ",seconds," seconds")
