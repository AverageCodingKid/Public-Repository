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
    
    
    #The records
    recordnames = ["Shea Lewis"]
    
    
    
    #Enter user's name

    askopenrec = str(input("Enter the name you are searching for: "))
    print("Searching 🔎")
    
    
    
    #Find
    if "Shea Lewis" in recordnames:
        print("Shea Lewis | Height: 4.10 Current net worth: $-200")
    
    #Name not found
    else:
        print("Could not locate user 🔘")


#Stay clear from this ☠
else:
    print("Access Denied ☠: Pc Lock Enabled 🔒")
    
    #Make a punishment here if the user gets the password wrong
    #One has already been placed under here
    # os.system("shutdown -r -t 0")


#Thank you if you have made it this far 🏆