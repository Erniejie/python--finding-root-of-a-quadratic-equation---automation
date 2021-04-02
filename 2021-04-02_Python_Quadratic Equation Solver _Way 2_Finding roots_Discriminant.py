#Quadratic Equation Solver in Python
# Find Roots of a Quadratic Equation - use of discriminant
#python- Computer Programming Tuttor- April 2, 2021

import math
a =float(input("Enter The Coefficient of a:"))
b =float(input("Enter The Coefficient of b:"))
c =float(input("Enter The Coefficient of c:"))

discriminant = b**2 -4*a*c

if discriminant >=0:
    x1= (-b + math.sqrt(discriminant))/2*a
    x2= (-b - math.sqrt(discriminant))/2*a
else:
    x1 = complex((-b/(2*a)),math.sqrt(-discriminant)/(2*a))
    x2 = complex((-b/(2*a)),-math.sqrt(-discriminant)/(2*a))

if discriminant > 0:
    print("It Has Two Distinct Real Roots: {} and {}".format(x1,x2))
elif discriminant == 0:
    print("It has double root:",x1)
else:
    print("It has Two Complex (Conjugate) Roots: {} and {}".format(x1,x2))
