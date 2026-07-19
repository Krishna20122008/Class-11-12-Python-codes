textfile=open("text.txt","w")
Lines=["Hello there!\n" ,"I have been learning file handling in python lately.\n","But it is a little bit hard to learn all the terms and it is also boring a bit.\n","Bye bye!\n"]
textfile.writelines(Lines)
textfile.close()

textfile=open("text.txt","r")
textfile.read()