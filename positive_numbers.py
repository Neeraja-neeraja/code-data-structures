#TASK 2
#to print all positive numbers in a range
list1=eval(input("Enter numbers: :"))
for num in list1:
    if num>=0:
        print(num, end= '  ')


list2=[12 , 14 , -95 , 3]
for num in list2:
    if num>=0:
        print(num, end= '  ')

#TASK 5
string=input("Enter:")
def most_frequent (string):
    d= dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
print most_frequent (string)
