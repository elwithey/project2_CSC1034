import csv

class Manage:

    def __init__(self):
        self.data= []
        self.fName = ""
        self.sName = ""
        self.title = ""
        self.gender = ""
        self.DOB = ""
        self.occupation = ""
        self.balance = int()
        self.overdraft = int()


    #retrieves a list of all data on all clients in the bank
    def retrieve(self):
        print(*self.data, sep ="\n")

    #appends the csv file to add a new client
    def append(self):
        self.fName = input("Please enter your first name")
        self.sName = input("Please enter your second name")
        self.title = input("Please enter your title e.g. Mr/Mrs")
        self.gender = input("Please enter your gender")
        self.DOB = input("Please enter your date of birth")
        self.occupation = input("Please enter your occupation")
        self.balance = input("Please enter your bank balance")
        self.overdraft = input("Please enter your preferred overdraft limit (maximum £5000)")



        with open ("MOCK_DATA.csv","a") as file:
            file.write("\n")
            file.write("")
            file.close()
        print(*(self.read()), sep ="\n")


    def read(self):

        with open("MOCK_DATA.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.data.append(row)

    def search(self):
        self.read()
        search = True
        while search:
            #reference
            self.fname = input("Please input your first name")
            column = [x[1] for x in self.data]
            if self.fname in column:
                for x in range(0,len(self.data)):
                    if self.fname == self.data[x][1]:

                        return (self.data[x],x)
            else:
                print("Name doesn't exist")
                repeat = True
                while repeat:
                    choice = input("Would you like to try again (T) or create a new account (A)?")
                    if choice == "A":
                        repeat = False
                        self.append()
                    elif choice == "T":
                        search = True
                        repeat = False
                    else:
                        print("Not an option")


    def checkBalance (self):
        balance = (self.search())
        # prints balance of client
        print(balance[0][7])

    def addMoney(self):
        information = (self.search())
        x = int(information[1])
        balance = int(information[0][7])

        amount = int(input("How much would you like to deposit into your account"))
        balance += amount
        self.data[x][7] = balance
        print(amount,"has been depositied into your account. Your balance is now",balance)

        quit = input("Would you like to perform any further actions? Y/N")
        return quit

#MAIN CODE -------------------------

if __name__ == "__main__":
    quit = False
    bank = Manage()
    print("WELCOME TO THE BANK")
    customer = input("Are you a new customer? Y/N  ")
    if customer == "Y":
        customer = input("Do you want to set up an account? Y/N  ")
        if customer == "Y":
            bank.append()

    else:
        customer = input("Are you an existing customer? Y/N  ")
        if customer == "Y":
            while not quit:
                print("")
                print("""
                MENU
                    1. CHECK BALANCE
                    2. WITHDRAW MONEY
                    3. ADD MONEY
                    4. LOG OUT
                Please pick 1,2,3 or 4.""")
                choice = input("")
                if choice == "1":
                    bank.checkBalance()
                    action = input("Would you like to perform any further actions? Y/N  ")

                elif choice == "3":
                    action = bank.addMoney()

                if action == "N":
                    quit = True
    print("Goodbye")













