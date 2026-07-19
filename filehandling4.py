import pickle
listvalues=[1,"Krishna",24,"CS Practical"]
list=open("cs.dat","ab")
pickle.dump(listvalues,list)
list.close()

list=open("cs.dat","rb")
a=pickle.load(list)
list.close()
print(a)