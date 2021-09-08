# python program to find the factorial of number

num=int(input("enter the number"))
fact=1
if num<0:
    print("factorial doesnot exist")
elif num ==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("the factorial", num, "is", fact)