#TASK 1
#fibonacci numbers
nterms=int(input("Enter the number of terms required : "))
n1=0
n2=1
count=0
if nterms<=0:
    print("Enter a positive integer")
elif nterms==0:
    print("Fibonacci series upto", nterms,":" , end='  ')
else:
    print("FIBONACCI SEQUENCE:")
    while count<nterms:
        print(n1)
        nth = n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1
