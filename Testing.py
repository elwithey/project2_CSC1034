from main import Manage

# import pytest
bank = Manage()


def addMoneyFail():
    print("Runs function addMoney.Enters a non-existent user")
    try:
        bank.addMoney(100, "Erin")
    except TypeError:
        print("Fails as expected")
    else:
        print("Passed unexpectedly")


def addMoneyPass():
    print("\n Runs function addMoney.Enters a user in the MOCK_DATA.csv file")
    try:
        bank.addMoney(100, "Edward")
    except TypeError:
        print("Fails Unexpectedly. Should find client named Edward and deposit £100")
    else:
        print("Passed as expected")


def addClientPass():
    print("\nRuns function append.Enters correct information to create a new user")

    try:
        bank.append("Erin", "Withey", "Miss", "Female", "8/20/2004", "Student", 5000, 300)
    except ValueError:
        message = "A variable passed to the Manage class is None, please check. Aborting creation of new client."
        print(message)
    else:
        print("Passed as expected")
        client = bank.searchName("Erin")
        print(client[0],"has now been added to the list")


def addClientFail1():
    print("\nRuns function append. Enters an invalid value for title column")

    try:
        bank.append("Erin", "Withey", None, "Female", "8/20/2004", "Student", 5000, 300)
    except ValueError:

        message = "Fails as expected. A variable passed to the Manage class is None, please check. Aborting creation " \
                  "of new client. "
        print(message)
    else:
        print("Passed unexpectedly")


def addClientFail2():
    print("\nRuns function addClient. Enters an a string for the balance value")

    try:
        bank.append("Erin", "Withey", "Miss", "Female", "8/20/2004", "Student", "5000", 300)
    except TypeError:
        message = "Fails as expected. Balance is not an integer, please check. Aborting creation of new client."
        print(message)
    else:
        print("yay")


def returnDOB():
    print("\nRuns function searchDOB. Prints clients with a birthday of 10/12/2002")
    dob = "10/12/2002"
    test = bank.searchDOB(dob)
    if test == "empty":
        print("NO CLIENTS WITH THAT DATE OF BIRTH")
    else:
        print("Clients details with birthday", dob, "are", test)


def deletePass():
    print("\nRuns function delete. Deletes client with name Hayden at position 91")
    try:
        bank.delete("Hayden")
        print("")
    except ValueError:
        message = "Unexpected fail"
        print(message)
    else:
        print("Test passed as expected")
        for i in range(0,len(bank.data)):
            print(bank.data[i])


def searchOverdraft():
    print("\nRuns function searchOverdraft. Finds clients who are over their overdraft")
    value = bank.searchOverdraft()
    for i in range(0, len(value)):
        print(value[i])


addMoneyFail()
addMoneyPass()
addClientPass()
addClientFail1()
addClientFail2()
returnDOB()
deletePass()
searchOverdraft()
