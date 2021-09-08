#python program to find the area of triangle
# A = 1/2 × b × h

a=5
b=6
c=7
#calculate the semi perimeter
s=(a+b+c)/2
#calculate the area
area=(s*(s-a)*(s-b)*(s-c)) **0.5
print("the are of triangle is ", area)