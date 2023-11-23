#frist task.1 "write a python program to count the number 4 in a given list"
list=[1,2,3,7,4,-2.3,4,5,4]
print(list.count(4))
                 #------------------------------------------#
# frist task.2 "write a python program to test whether a passed letter is a vowel or not"
letter=input("enter the letter: ")
ls=['a','i','o','u','e']
if letter in ls:
    print("vowel")
else:
    print("not vowel")
                  #------------------------------------------#
# frist task.3 "write a python program to access environment variables"
import os
path=os.environ['PATH']
print(path)
                 #------------------------------------------#
#second task "write a python program which accepts the radius of the circle from the user and calculate area"
import math as m
r=int(input("Enter your radius:"))
#area=m.pi*r**2             
#print("area_of circle: ",area)    
print("area_circle: ",m.pi*r**2)
                 #------------------------------------------#
#third task "write a program to print the calendar of a given month and year"
import calendar
year=int(input("year:"))
month=int(input("month:"))
print(calendar.month(year,month))