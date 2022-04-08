#TASK  1
p=3.14
r=eval(input("Input the radius of the circle: "))
area=p*r**2
print("The area of the circle with radius",r, "is : ", area)


#TASK 2
filename=input("Input the filename: ")
f_ext=filename.split(".")
print("The extension of the file is " +repr(f_ext[-1]))

