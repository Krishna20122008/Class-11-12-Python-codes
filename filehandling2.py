myobject=open("myfile.txt","w")
list=["Hello there!\n" ,"I have been learning file handling in python lately.\n","But it is a little bit hard to learn all the terms and it is also boring a bit.\n","Bye bye!\n"]
myobject.writelines(list)
myobject.close()
myobject=open("myfile.txt","r")
print(myobject.read())