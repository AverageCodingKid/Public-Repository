import os
#Context
print("Welcome, this is a test code. Do not worry if your pc restarts after an incorrect password, everthing is ok.")
#Passes
passwords = ["L3PALMERS", "E=MC^2", "123"]
guess = str(input("Enter the password: "))

#If you have guessed the password you will be granted access.
if guess in passwords:
    
    #Granted Access
    print("Access Granted ✅")
    
    
    #The first record
    shearecord = ["Shea Lewis | Height: 4.10 Current net worth: $-200"]
    
    
    
    #Enter user's name

    askopenrec = str(input("Enter the name you are searching for: "))
    print("Searching 🔎")
    
    
    
    #Find
    if "Name: Shea Lewis" in shearecord:
        print(shearecord)
    
    #Name not found
    else:
        print("Could not locate user 🔘")


#Stay clear from this ☠
else:
    print("Access Denied ☠: Pc Lock Enabled 🔒")
    os.system("shutdown -r -t 00")


#Thank you if you have made it this far 🏆