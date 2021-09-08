#program to display the Fibonacci series upto nth term and n is provided by the user

#nterms=10
nterms=int(input("how many terms ?"))
#first two numbers
n1 = 0
n2 = 1
count = 0
#check if number of terms is valid
if nterms < 0:
    print("please enter the positive integer")
elif nterms == 1:
    print("Fibonacci series upto",nterms,":")
    print(n1)
else:
    print("Fibonacci series upto",nterms,":")
    while count<nterms:
        print(n1,end=' , ')
        nth = n1+n2
        #update values
        n1=n2
        n2=nth
        count += 1