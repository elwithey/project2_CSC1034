# project2_CSC1034
### Running The Code
My Main code lies in main.py which includes the class Manage. Manage holds all methods that allow a user to create 
changes to the CSV file (MOCK_DATA.csv) and lets the user view details about clients.
To run tests on the main code, the user must run Testing.py which will automatically run through all tests for every 
method. The tests will indicate which method has been run and whether the test is supposed to pass or fail.
Some methods will also print out parts of the csv to prove functionality.

### User Validation
Balance: whenever a value is entered into the column balance the tests will confirm it is an integer otherwise it will 
raise a type error
Overdraft: a clients' overdraft must be over £0 and also an integer. The tests addClientsFail2 and addClientsFail3
confirm that this user validation works correctly
Date of Birth: a clients date of birth must be entered as a string the tests will validate this whenever date of birth 
is inputted

### Sensitivity
I chose to make my string inputs case-sensitive as it will reduce the likelihood of repeating data as it makes 
comparisons easier

### User Examples
#### Search for all clients with a negative balance:
No input from the user. 
Once the method is run the program will search through the list self.data
and whenever a clients balance is below 0 it will be added to another list called
final which will then be printed out.
If there are no users with a negative balance then the program will print 'NO CLIENTS WITH NEGATIVE BALANCE'

#### Edit a clients occupation
The user must input their firstname and their new occupation.
The program will then tell them their current occupation and then inputs their new
occupation into the list. The program then tells the user that their occupation ahs been changed

#### Depositing money into a bank account
The user must input their firstname and the amount they wish to deposit into their account.
If the user doesn't exist in the csv file then the program raises an error.
If the user does exist then the program will print the current balance and then the
new balance once it has been changed in the list