import csv


class Manage():

    def __init__(self):
        self.data = []
        self.fName = ""

    # retrieves a list of all data on all clients in the bank
    def retrieve(self):
        self.read()
        for i in range(0,len(self.data)):
            print(self.data[i])

    #appends the csv file to add a new client
    def append(self, fName, sName, title, gender, DOB, occupation, balance, overdraft):
        self.read()
        if (self.fName == None) or (sName == None) or (title == None) or (gender == None) or (DOB == None) or (
                occupation == None) or (balance == None) or (overdraft == None):
            # If we find a variable which is None, raise an Exception
            raise ValueError()
        if not isinstance(balance, int) or not isinstance(overdraft, int):
            raise TypeError()

        data_len = len(self.data)
        client_id = data_len + 1
        self.data.append([(str(client_id)), self.fName, sName, title, gender, DOB, occupation, (str(balance)), (str(overdraft))])
        for i in range(0, len(self.data)):
            print(self.data[i])


    def read(self):

        with open("MOCK_DATA.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.data.append(row)

    def search(self):
        self.read()
            #reference
            column = [x[1] for x in self.data]
            if self.fname in column:
                for x in range(0,len(self.data)):
                    if self.fname == self.data[x][1]:
                        return self.data[x]


    def checkBalance (self):
        balance = (self.search())
        # prints balance of client
        return balance[0][7]

    def addMoney(self):
        def addMoney(self, amount, fName):
            information = (self.search(fName))
            if information is None:
                raise TypeError
            x = int(information[0])
            balance = int(information[7])
            balance += amount
            self.data[x][7] = balance
            print(amount, "has been deposited into the account. The balance is now", balance)


def withdrawMoney(self):
        information = (self.search())
        x = int(information[1])
        balance = float(information[0][7])
        overdraft = int(information[0][8])
        overdraft = -abs(overdraft)


        amount = float(input("How much would you like to withdraw from the account"))
        balance -= amount
        self.data[x][7] = balance
        print(amount, "has been withdrawn from the account. The balance is now", balance)
        if balance < overdraft:
            balance -= 5
            self.data[x][7] = balance
            print("£5 has been charged to the account for going over your overdraft limit. The balance is now ", balance)

        quit = input("Would you like to perform any further actions? Y/N")
        return quit


    def getPassword(self):
        return self.password

    def delete(self):
        information = (self.search())
        position = int(information[1])
        print(position)
        self.data.pop(position)
        for i in range(0, len(self.data)):
            print(self.data[i])
        quit = input("Would you like to perform any further actions? Y/N")
        return quit

    def edit(self):
        information = self.search()
        x = int(information[1])
        print("""
        WHICH DETAIL WOULD YOU LIKE TO EDIT
        
        1. FIRST NAME
        2. SECOND NAME
        3. DATE OF BIRTH
        4. OCCUPATION
        5. BALANCE
        6. OVERDRAFT""")
        choice = input("")
        if choice == "1":
            self.data[x][int(choice)] = input("Please input the new forename")
        elif choice == "2":
            self.data[x][int(choice)] = input("Please input the new surname")
        elif choice == "3":
            self.data[x][int(choice)] = input("Please input the new date of birth. Format: M/D/YYYY")
        elif choice == "4":
            self.data[x][int(choice)] = input("Please input the new occupation")
        elif choice == "5":
            balance = float(input("Please input the new balance"))
            self.data[x][int(choice)] = str(balance)
        elif choice == "6":
            overdraft = int(input("Please input the new overdraft. Limit is £500"))
            self.data[x][int(choice)] = str(overdraft)

        print(information[0])
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
                Please pick 1,2,3 or 4.""")
                choice = input("")
                if choice == "1":
                    bank.checkBalance()
                    action = input("Would you like to perform any further actions? Y/N  ")
                elif choice == "2":
                    action = bank.withdrawMoney()

                elif choice == "3":
                    action = bank.addMoney()

                if action == "N":
                    quit = True
        if customer == "N":
            user = input("Are you an admin? Y?N  ")
            password = input("Please input the admin password")
            if user == "Y" and password == "no":
                while not quit:
                    print("""
                                    MENU
                                        1. CHECK BALANCE
                                        2. WITHDRAW MONEY
                                        3. ADD MONEY
                                        4. DELETE CLIENT
                                        5. EDIT DETAILS
                                        6. SEE ALL CLIENTS
                                    Please pick 1,2,3 or 4.""")
                    choice = input("")
                    action = ""
                    if choice == "1":
                        adminUser.checkBalance()
                        action = input("Would you like to perform any further actions? Y/N  ")

                    elif choice == "2":
                        action = adminUser.withdrawMoney()

                    elif choice == "3":
                        action = adminUser.addMoney()
                    elif choice == "4":
                        action = adminUser.delete()
                    elif choice == "5":
                        action = adminUser.edit()
                    elif choice == "6":
                        action = adminUser.retrieve()
                    if action == "N":
                        quit = True

            if password != adminUser.getPassword():
                print("Incorrect Password")
    print("Goodbye")













