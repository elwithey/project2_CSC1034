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

    # appends the list self.data to add a new client at the end of the list
    def append(self, fName, sName, title, gender, DOB, occupation, balance, overdraft):
        if (fName is None) or (sName is None) or (title is None) or (gender is None) or (DOB is None) or \
                (occupation is None) or (balance is None) or (overdraft is None):
            # If it finds a variable which is None, raise an Exception
            raise ValueError()
        # if balance or overdraft are not integers then a TypeError is raised
        if not isinstance(balance, int) or not isinstance(overdraft, int):
            raise TypeError()
        if overdraft < 0:
            return False
        # adds the inputted information to the list
        data_len = len(self.data)
        # creates a new client_id by adding 1 to the last client_id
        client_id = data_len + 1
        self.data.append([(str(client_id)), fName, sName, title, gender, DOB, occupation, (str(balance)),
                          (str(overdraft))])


    def read(self):
        # reads the csv file and turns it into a list
        with open("MOCK_DATA.csv", "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                self.data.append(row)

# searches for a clients details using their firstname
    def searchName(self, fName):
        # adapted from
        # https://www.youtube.com/watch?v=0QNzEKRTfck&t=168s
        column = [x[1] for x in self.data]
        if fName in column:
            for x in range(0, len(self.data)):
                # checks if the name inputted is equal to the current firstname
                if fName == self.data[x][1]:
                    return self.data[x], x

# searches for clients with a certain date of birth
    def searchDOB(self, DOB):
        final = []
        column = [x[5] for x in self.data]
        if DOB in column:
            for x in range(0, len(self.data)):
                if DOB == self.data[x][5]:
                    # adds any clients with the date of birth being searched for to the list final
                    final.append(self.data[x])
        # if no clients have the date of birth then the client is informed of this
        if len(final) == 0:
            return "empty"
        return final



    def searchNegative(self):
        # searches for clients with a negative balance
        final = []
        for x in range(0, len(self.data)):
            if float(self.data[x][7]) < 0:
                final.append(self.data[x])
        # if no clients have a negative balance then the client is informed
        if len(final) == 0:
            return "NO CLIENTS WITH NEGATIVE BALANCE"
        return final


    def checkBalance(self, fName):
        # returns balance of client
        balance = (self.searchName(fName))
        if balance is None:
            raise TypeError
        return balance[0][7]

    def addMoney(self, amount, fName):
        # deposits money into the clients account
        information = (self.searchName(fName))
        # if the name is not found in the file a TypeError is raised
        if information is None:
            raise TypeError
        x = int(information[1])
        balance = int(information[0][7])
        print(balance,"is your current balance")
        # adds the amount deposited onto the existing balance
        balance += amount
        self.data[x][7] = balance
        print(amount, "has been deposited into the account. The balance is now", balance)

    def withdrawMoney(self,amount, fName):
        # takes money off a clients current balance
        information = (self.searchName(fName))
        x = int(information[1])
        balance = float(information[0][7])
        overdraft = int(information[0][8])
        overdraft = -abs(overdraft)

        print(balance,"is your current balance")
        balance -= amount
        self.data[x][7] = balance
        print(amount, "has been withdrawn from the account. The balance is now", balance)
        # if a client is in their overdraft then they are charged an extra £5 for every new withdrawal request
        # until they are no longer in their overdraft
        if balance < overdraft:
            balance -= 5
            self.data[x][7] = balance
            print("£5 has been charged to the account for going over your overdraft limit. The balance is now ",
                  balance)

    def delete(self, fName):
        # deletes a clients' information from the list
        information = (self.searchName(fName))
        position = int(information[1])
        self.data.pop(position)
        return self.data

    def editfName(self, fName, newfName):
        # edits the firstname of the client
        information = self.searchName(fName)
        print(fName,"is your current first name")
        x = int(information[1])
        self.data[x][1] = newfName
        print(self.data[x][1],"is your new first name")


    def editsName(self, fName, newsName):
        # changes a clients' surname
        information = self.searchName(fName)
        x = int(information[1])
        print(self.data[x][2], "is your current last name")
        x = int(information[1])
        self.data[x][2] = newsName
        print(self.data[x][2], "is your new last name")


    def editOccupation(self, fName,newOccupation):
        # edits a clients' occupation
        information = self.searchName(fName)
        x = int(information[1])
        print(self.data[x][6], "is your current occupation name")
        x = int(information[1])
        self.data[x][6] = newOccupation
        print(self.data[x][6], "is your new occupation name")


    def editDOB(self, fName,newDOB):
        # edits the clients' date of birth
        # if the date of birth is not entered a string an error is raised
        if not isinstance(newDOB, str):
            raise TypeError
        information = self.searchName(fName)
        x = int(information[1])
        print(self.data[x][5], "is your current date of birth")
        x = int(information[1])
        self.data[x][5] = newDOB
        print(self.data[x][5], "is your new date of birth")


    def editOverdraft(self, fName, newOverdraft):
        # changes the clients' overdraft limit
        # if overdraft is not entered as an integer a TypeError is raised
        if not isinstance(newOverdraft, int):
            raise TypeError
        information = self.searchName(fName)
        x = int(information[1])
        print(self.data[x][8], "is your current overdraft limit")
        x = int(information[1])
        self.data[x][8] = str(newOverdraft)
        print(self.data[x][8], "is your new overdraft limit")

# adapted from
# https://www.programiz.com/python-programming/writing-csv-files
    def write(self):
        # writes the data in self.data to the csv file to save any changes made
        with open('MOCK_DATA.csv','w',newline='') as f:
            write = csv.writer(f)
            for i in range(0,len(self.data)):
                write.writerow(self.data[i])
