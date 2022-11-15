import testingfile as T
#import pytest

def test():
    try:
        T.addMoney(100,"Edward")
    except:
        print("Fails but not supposed to")
    else:
        ("YAY")

test()