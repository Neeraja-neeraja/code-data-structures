#methods of dictionary
#clear()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.clear()
print(car)

#copy()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.copy()
print(x)

#fromkeys()
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#get()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.get("model")
print(x)

#items()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.items()
print(x)

#keys()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.keys()
print(x)

#pop()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.pop("model")
print(car)

#popitem()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.popitem()
print(car)

#setdefault()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.setdefault("model", "Bronco")
print(x)

#update()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.update({"color": "White"})
print(car)

#values()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.values()
print(x)

#methods of string
#capitalise()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#casefold()
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode()
txt = "My name is Ståle"
x = txt.encode()
print(x)

#find()
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#index()
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

#isdigit()
txt = "50800"
x = txt.isdigit()
print(x)

#islower()
txt = "hello world!"
x = txt.islower()
print(x)

#add to tuple
T1=(10,50,20,9,40,25,60,30,1,56)
L1=list(T1)
L1
[10, 50, 20, 9, 40, 25, 60, 30, 1, 56]
L1.append(100)
T1=tuple(L1)
T1
(10, 50, 20, 9, 40, 25, 60, 30, 1, 56, 100)

#pattern

# Reading number of rows
row = int(input("Enter number of rows: "))

print("Generated Hourglass Pattern is: ")
# Upper-half
for i in range(row, 0, -1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

# Lower-half
for i in range(2, row+1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()

