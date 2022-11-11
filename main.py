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
        self.fname = input("Please input your first name")
        column = [x[1] for x in self.data]
        if self.fname in column:
            for x in range(0,len(self.data)):
                if self.fname == self.data[x][1]:

                    return self.data[x]
        else:
            print("Name doesn't exist")

    def checkBalance (self):
        balance = self.search()
        print(balance[7])

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
                print("MENU")
                print("""
                    1. CHECK BALANCE
                    2. WITHDRAW MONEY
                    3. ADD MONEY
                    4. LOG OUT
                Please pick 1,2,3 or 4.""" )
                choice = input("")
                if choice == "1":
                    bank.checkBalance()
                    choice = input("Would you like to perform any further actions? Y/N  ")
                    if choice == "N":
                        quit = True
    print("Goodbye")













