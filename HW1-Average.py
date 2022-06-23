from lib2to3.pgen2.token import GREATER


Name=input("Enter your name: ")
Family=input("Enter your family name: ")
A=float(input("Enter course A score: "))
B=float(input("Enter course B score: "))
C=float(input("Enter course C score: "))

Average= (A+B+C)/3

if Average>=17:
    status="great"
if Average<17 and Average>=12:
    status="normal"
if Average<12:
    status="fail"
print("Average: ",Average," Status: ",status)