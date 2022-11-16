from main import Manage
# import pytest
bank = Manage()

def test():

    try:
        bank.addMoney(100,"Erin")
    except TypeError:
        print("Fails as expected")
    else:
        print("Passed unexpectedly")


def test2():
    try:
        bank.append("Erin","Withey","Miss","Female","8/20/2004","Student",5000,300)
    except ValueError:
        message = "A variable passed to the Manage class is None, please check. Aborting creation of new client."
        print(message)
    else:
        print("Passed unexpectedly")


def test3():
    try:
        bank.append("Erin","Withey",None,"Female","8/20/2004","Student",5000,300)
    except ValueError:

        message = "Fails as expected. A variable passed to the Manage class is None, please check. Aborting creation " \
                  "of new client. "
        print(message)
    else:
        print("yay")


def test4():
    try:
        bank.append("Erin","Withey","Miss","Female","8/20/2004","Student","5000",300)
    except TypeError:

        message = "Balance is not an integer, please check. Aborting creation of new client."
        print(message)
    else:
        print("yay")


test2()
test()
test3()
test4()