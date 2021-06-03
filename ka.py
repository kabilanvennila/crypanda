mysal= float(input("Enter the Salary: "))
mylevel = int(input("Enter the Level: ")) 

if(mylevel==3):
    print("The Salary will is: "+str(mysal+(mysal*0.15)))
elif(mylevel==4):
    print("The Salary will is: "+str(mysal+(mysal*0.07)))
elif(mylevel==5):
    print("The Salary will is: "+str(mysal+(mysal*0.05)))
else: 
    print("The Salary will is: "+str(mysal))