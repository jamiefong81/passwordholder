

status = True

def display():
   print ("Do you want to add a password or get a password? get/add (q to quit)")
   global response
   response = input()
   if response == "add":
      savingPasswords()
   elif response == "get":
      getPassword()
   elif response == "q":
      quit()

def savingPasswords():
   with open('passwords.csv','a') as f:
      account = input("What account is this for? ")
      username = input("Enter username: ")
      password = input("Enter password: ")
      f.write(f"{account},{username},{password}\n")
   print("Login successfully saved!")


def getPassword():
   with open("passwords.csv", "r") as f:
      account = input("What account is this for? ")
      lines = f.readlines()
      for line in lines:
         if line.startswith(account):
            data = line.strip().split(",")
            print(f"Your username: {data[1]}\nYour password: {data[2]}")

while status == True:
   display()


def quit():
   if response == "q":
      status = False
