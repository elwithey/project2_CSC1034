class Manage():

    def __init__(self,data):
        self.data = data

    #adds a new client to the current bank clients
    def add(self):
        self.data.append("")
        print(*self.data, sep ="\n")

    def retrieve(self):
        print(*self.data, sep ="\n")



#opens the clients' data from a csv file
f = open("MOCK_DATA.csv","r")
data = f.readlines()

#turns data into a list
for i in range(len(data)):
    #takes away whitespace
    data[i] = data[i].strip()

bank = Manage(data)
bank.add()
bank.retrieve()




