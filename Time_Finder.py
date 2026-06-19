#This is a python code to find the time to reach the destination by taking distance and speed input from the user..

Distance=int(input("Enter the distance to be travelled: "))
Speed=int(input("Enter average speed with which vehicle is travelling: "))
Time=Distance/Speed
print("Distance is ",Distance, " km")
print(f"Speed is {Speed} kmph")
print("Time taken: ",Time," hr")
