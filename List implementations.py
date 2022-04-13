#list implementation

#creating a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#accessing a list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#negative indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# checking if the item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#replacing by inserting new values
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#delete
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clear
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



