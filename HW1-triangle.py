A=input("Enter first triangle side: ")
B=input("Enter second triangle side: ")
C=input("Enter third triangle side: ")

if C<A+B and A<B+C and B<A+C:
    print("It is possible to draw a triangle with ",A,",",B,",",C ," sides")
else:
    print("It is NOT possible to draw a triangle with ",A,",",B,",",C ," sides")