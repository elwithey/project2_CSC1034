from main import Manage

bank = Manage()


def seeAllData():
    print("Runs method retrieve. Prints list of all clients and all details")
    bank.retrieve()


def addMoneyFail():
    print("\nRuns method addMoney.Deposits money into a users account")
    try:
        bank.addMoney(100, "Annie")
    except TypeError:
        print("Fails as expected")
    else:
        print("Passed unexpectedly")


def addMoneyPass():
    print("\nRuns method addMoney.Deposits money into a users account")
    try:
        bank.addMoney(100, "Edward")
    except TypeError:
        print("Fails Unexpectedly. Should find client named Edward and deposit £100")
    else:
        print("Passed as expected")


def withdrawalPass():
    print("\nRuns method withdrawMoney.Withdraws money from a users account")
    try:
        bank.withdrawMoney(100, "Tanisha")
    except TypeError:
        print("Fails Unexpectedly. Should find client named Tanisha and withdraw £100")
    else:
        print("Passed as expected")


def withdrawalFail1():
    print("\nRuns method withdrawMoney.Withdraws money from a users account")
    try:
        bank.withdrawMoney(100, "Annie")
    except TypeError:
        print("Fail as expected as user does not exist")
    else:
        print("Passed unexpectedly")


def withdrawalFail2():
    print("\nRuns method withdrawMoney.Withdraws money from a users account who goes over overdraft so is charged £5")
    try:
        bank.withdrawMoney(100, "Edward")
    except TypeError:
        print("Failed unexpectedly")
    else:
        print("Passed as expected")


def searchNamePass():
    print("\nRuns method SearchName. Searches CSV file for a client by their first name")
    try:
        test = bank.searchName("Catherine")
    except ValueError:
        print("Fails unexpectedly. Should return data for client with name Catherine")
    else:
        print("Passed as expected")
        print(test[0])


def searchNameFail():
    print("\nRuns method SearchName. Searches CSV file for a client by their first name")
    test = bank.searchName("Annie")
    if test is None:
        print("Fails as expected")
    else:
        print("Passed unexpectedly. Should fail as name Annie not in csv file")
        print(test[0])


def addClientPass():
    print("\nRuns method append.Enters correct information to create a new user")
    try:
        bank.append("Erin", "Withey", "Miss", "Female", "8/20/2004", "Student", 5000, 300)
    except ValueError:
        message = "A variable passed to the Manage class is None, please check. Aborting creation of new client."
        print(message)
    else:
        print("Passed as expected")
        client = bank.searchName("Erin")
        print(client[0], "has now been added to the list")


def addClientFail1():
    print("\nRuns method append. Enters an invalid value for title column")

    try:
        bank.append("Erin", "Withey", None, "Female", "8/20/2004", "Student", 5000, 300)
    except ValueError:

        message = "Fails as expected. A variable passed to the Manage class is None, please check. Aborting creation " \
                  "of new client. "
        print(message)
    else:
        print("Passed unexpectedly")


def addClientFail2():
    print("\nRuns method addClient. Enters an a string for the balance value")

    try:
        bank.append("Erin", "Withey", "Miss", "Female", "8/20/2004", "Student", "5000", 300)
    except TypeError:
        message = "Fails as expected. Balance is not an integer, please check. Aborting creation of new client."
        print(message)
    else:
        print("Passed when should have failed")


def addClientFail3():
    print("\nRuns method addClient. Enters an a string for the balance value")

    try:
        bank.append("Erin", "Withey", "Miss", "Female", "8/20/2004", "Student", "5000", -200)
    except TypeError:
        message = "Fails as expected. Overdraft is below 0, please check. Aborting creation of new client."
        print(message)
    else:
        print("passed when expected fail")


def returnDOBPass():
    print("\nRuns method searchDOB. Prints clients with a birthday of 10/12/2002")
    dob = "10/12/2002"
    test = bank.searchDOB(dob)
    if test == "empty":
        print("NO CLIENTS WITH THAT DATE OF BIRTH")
    else:
        print("Clients details with birthday", dob, "are", test)


def returnDOBFail():
    print("\nRuns method searchDOB. Prints clients with a birthday of 08/20/2004")
    dob = "08/20/2004"
    test = bank.searchDOB(dob)
    if test == "empty":
        print("NO CLIENTS WITH THAT DATE OF BIRTH")
    else:
        print("Clients details with birthday", dob, "are", test)


def deletePass():
    print("\nRuns method delete. Deletes client with name Hayden at position 91")
    try:
        bank.delete("Hayden")
    except ValueError:
        print("Unexpected fail")
    else:
        print("Test passed as expected")
        for i in range(0, len(bank.data)):
            print(bank.data[i])


def checkBalancePass():
    print("\nRuns method checkBalance. Finds the balance of a specific client")
    try:
        test = bank.checkBalance("Faaris")
    except TypeError:
        print("Fails unexpectedly")
    else:
        print("Passed as expected.")
        print(test)


def checkBalanceFail():
    print("\nRuns method checkBalance. Finds the balance of a specific client")
    try:
        test = bank.checkBalance("Annie")
    except TypeError:
        print("Fails as expected as username is not in csvfile")
    else:
        print("Passed unexpectedly as name should not be found")
        print(test)


def searchNegative():
    print("\nRuns method searchNegative. Finds clients who have a negative balance")
    value = bank.searchNegative()
    for i in range(0, len(value)):
        print(value[i])


def editfNamePass():
    print("\nRuns method editfName.  Edits clients registered first name")
    try:
        bank.editfName("Edward", "Roman")
    except NameError:
        print("Unexpected error")
    else:
        print("Passed Successfully")


def editfNameFail():
    print("\nRuns method editfName.  Edits clients registered first name")
    try:
        bank.editfName("Edward", Roman)
    except NameError:
        print("Expected error as a value is not a string")
    else:
        print("Unexpected Pass")


def editsNamePass():
    print("\nRuns method editsName.  Edits clients registered surname name")
    try:
        bank.editsName("Roman", "Ahearn")
    except NameError:
        print("Unexpected error")
    else:
        print("Passed Successfully")


def editsNameFail():
    print("\nRuns method editsName. Edits clients registered surname name")
    try:
        bank.editsName("Roman", Ahearn)
    except NameError:
        print("Expected error as a value is not a string")
    else:
        print("Unexpected Pass")


def editOccupationPass():
    print("\nRuns method editOccupation.  Edits clients registered occupation")
    try:
        bank.editOccupation("Roman", "CustomerAssistant")
    except NameError:
        print("Unexpected error")
    else:
        print("Passed Successfully")


def editOccupationFail():
    print("\nRuns method editOccupation. Edits clients registered occupation")
    try:
        bank.editOccupation("Roman", CustomerAssistant)
    except NameError:
        print("Expected error as a value is not a string")
    else:
        print("Unexpected Pass")


def editDOBPass():
    print("\nRuns method editDOB.  Edits clients registered date of birth")
    try:
        bank.editDOB("Roman", "5/7/2003")
    except NameError:
        print("Unexpected error")
    else:
        print("Passed Successfully")


def editDOBFail():
    print("\nRuns method editDOB. Edits clients registered date of birth")
    try:
        bank.editDOB("Roman", 5 / 7 / 2003)
    except TypeError:
        print("Expected error as a value is not a string")
    else:
        print("Unexpected Pass")


def editOverdraftPass():
    print("\nRuns method editOverdraft.  Edits clients registered overdraft")
    try:
        bank.editOverdraft("Roman", 3000)
    except NameError:
        print("Unexpected error")
    else:
        print("Passed Successfully")


def editOverdraftFail():
    print("\nRuns method editOverdraft. Edits clients registered overdraft")
    try:
        bank.editOverdraft("Roman", "3000")
    except TypeError:
        print("Expected error as a value is not a string")
    else:
        print("Unexpected Pass")


def savedata():
    bank.write()


seeAllData()
addMoneyFail()
addMoneyPass()
addClientPass()
addClientFail1()
addClientFail2()
addClientFail3()
returnDOBPass()
returnDOBFail()
deletePass()
searchNegative()
searchNamePass()
searchNameFail()
checkBalancePass()
checkBalanceFail()
withdrawalPass()
withdrawalFail1()
withdrawalFail2()
editfNamePass()
editfNameFail()
editsNamePass()
editsNameFail()
editOccupationPass()
editOccupationFail()
editDOBPass()
editDOBFail()
editOverdraftPass()
editOverdraftFail()
savedata()
