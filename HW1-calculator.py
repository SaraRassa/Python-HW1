import math

A=float(input("Enter desired number: "))
OP=input("Enter desired operation: ")

if OP=="+":
    B=int(input("Enter second number: "))
    result=A+B
if OP=="-":
    B=float(input("Enter second number: "))
    result=A-B
if OP=="*":
    B=float(input("Enter second number: "))
    result=A*B
if OP=="/":
    B=float(input("Enter second number: "))
    if B==0:
            result="Errot"
    else:
        result=A/B
if OP=="sqrt":
    result=math.sqrt(A)
if OP=="sin":
    result=math.sin(math.radians(A))
if OP=="cos":
    result=math.cos(math.radians(A))
if OP=="tan":
    result=math.tan(math.radians(A))
if OP=="cot":
    result=1/math.tan(math.radians(A))
if OP=="!":
    result=math.factorial(round(A))

print(result)
