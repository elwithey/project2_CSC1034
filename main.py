
class Manage():

    def __init__(self):
        self.fName = input("Please enter your first name")
        self.sName = input("Please enter your second name")
        self.title = input("Please enter your title e.g. Mr/Mrs")
        self.gender = input("Please enter your gender")
        self.DOB = input("Please enter your date of birth")
        self.occupation = input("Please enter your occupation")
        self.balance = input("Please enter your bank balance")
        self.overdraft = input("Please enter your preferred overdraft limit (maximum £5000)")

    #retrieves a list of all data on all clients in the bank
    def retrieve(self):
        print(*(self.read()), sep ="\n")

    #appends the csv file to add a new client
    def append(self):



        with open ("MOCK_DATA.csv","a") as file:
            file.write("\n")
            file.write("")
            file.close()
        print(*(self.read()), sep ="\n")


    def read(self):
        # opens the clients' data from a csv file
        f = open("MOCK_DATA.csv", "r")
        data = f.readlines()
        f.close()

        # turns data into a list
        for i in range(len(data)):
            # takes away whitespace
            data[i] = data[i].strip()
        return data

if __name__ == "__main__":
    print("WELCOME TO THE BANK")
    customer = input("Are you a new customer? Y/N  ")
    if customer == "Y":
        customer = input("Do you want to set up an account? Y/N  ")
        if customer == "Y":
            bank = Manage()
            bank.append()
        else:
            print("Goodbye")
    else:
        type = input("Are you an existing customer? Y/N  ")
        
        if type == "Y":
            print("MENU")
            print("""
                1. CHECK BALANCE
                2. WITHDRAW MONEY
                3. ADD MONEY
                4. LOG OUT
            Please pick 1,2,3 or 4.""" )
            choice = input("")
            if choice == "1":











