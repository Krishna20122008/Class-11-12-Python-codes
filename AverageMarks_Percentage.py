#This is a python code to find the average marks of a student in his/her exam and to find the percentage..

maths=float(input("enter the value of maths:"))
bio=float(input("enter the value of bio:"))
physics=float(input("enter the value of physics:"))
chem=float(input("enter the value of chem:")) 
Eng=float(input("enter the value of Eng:")) 
print("average of marks of five subjects is:", ((maths+bio+physics+chem+Eng)/5))
print("percentage of child is:", (((maths+bio+physics+chem+Eng)/400)*100) ,"%")
