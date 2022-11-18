import csv


class Manage:

    def __init__(self):
        self.data = []
        self.read()
        self.fName = ""

    # retrieves a list of all data on all clients in the bank
    def retrieve(self):
        for i in range(0, len(self.data)):
            print(self.data[i])

    # appends the csv file to add a new client
    def append(self, fName, sName, title, gender, DOB, occupation, balance, overdraft):
        if (fName is None) or (sName is None) or (title is None) or (gender is None) or (DOB is None) or \
                (occupation is None) or (balance is None) or (overdraft is None):
            # If we find a variable  which is None, raise an Exception
            raise ValueError()
        if not isinstance(balance, int) or not isinstance(overdraft, int):
            raise TypeError()

        data_len = len(self.data)
        client_id = data_len + 1
        self.data.append([(str(client_id)), fName, sName, title, gender, DOB, occupation, (str(balance)),
                          (str(overdraft))])

    def read(self):

        with open("MOCK_DATA.csv", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                self.data.append(row)

    def searchName(self, fName):
        # reference
        column = [x[1] for x in self.data]
        if fName in column:
            for x in range(0, len(self.data)):
                if fName == self.data[x][1]:
                    return self.data[x], x


    def searchDOB(self, DOB):
        final = []
        # reference
        column = [x[5] for x in self.data]
        if DOB in column:
            for x in range(0, len(self.data)):
                if DOB == self.data[x][5]:
                    final.append(self.data[x])
        if len(final) == 0:
            return "empty"
        return final

    def searchNegative(self):
        final = []
        for x in range(0, len(self.data)):
            if float(self.data[x][7]) < 0:
                final.append(self.data[x])
        if len(final) == 0:
            return "NO CLIENTS IN OVERDRAFT"
        return final

    def checkBalance(self, fName):
        balance = (self.searchName(fName))
        # prints balance of client
        if balance is None:
            raise TypeError
        return balance[0][7]

    def addMoney(self, amount, fName):
        information = (self.searchName(fName))
        if information is None:
            raise TypeError
        x = int(information[1])
        balance = int(information[0][7])
        balance += amount
        self.data[x][7] = balance
        print(amount, "has been deposited into the account. The balance is now", balance)

    def withdrawMoney(self, fName):
        information = (self.searchName(fName))
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
            print("£5 has been charged to the account for going over your overdraft limit. The balance is now ",
                  balance)

    def delete(self, fName):
        information = (self.searchName(fName))
        # if information is None:
        # raise ValueError
        position = int(information[1])
        self.data.pop(position)
        return self.data

    def edit(self, fName):
        information = self.searchName(fName)
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
