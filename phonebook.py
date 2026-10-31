import sys
def initial_phonebook():
    rows,cols=int(input("enter initial number of contacts : ")),5
    phonebook=[]
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact %d detail in the following orders(ONLY):" %(i+1))
        print(" Note: * indicates mandatary fields")
        print("..........................................................")
        temp=[]
        for j in range(cols):
            if j ==0:
                temp.append(str(input("Enter name * = ")))
                if temp[j]=="" or temp[j]==" ":
                    sys.exit("Name is mandatory field. Exiting due to blank field...")