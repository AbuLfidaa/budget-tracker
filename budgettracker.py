# we create an empty list to store our data
transHistory = []

while True:
    try:
        menu = int(input("1. Add income""\n" "2. Add expense" "\n" "3. View balance" "\n" "4. View transaction history" "\n" "5. Quit "))
    except:
        print("Enter a number!")
        continue
    # An empty dictionary in the loop to store any transaction type with the key and corresponding value
    dic = {}
    

    if menu == 5:
        print("Goodbye!")
        break
    elif menu == 1:
        incomeAmount = int(input("Income amount: "))
        dic["type"] = "income"
        dic["amount"] = incomeAmount
        
        # every dictionary should be added (appended) to the empty transaction history
        transHistory.append(dic)
        continue

    elif menu == 2:
        expenseAmount = int(input("Add expense?"))
        dic["type"] = "expense"
        dic["amount"] = expenseAmount
        transHistory.append(dic)
        continue
    elif menu == 3:
        balance = 0
        # sub = 0
        for transaction in transHistory:
                if transaction["type"] == "income":
                    balance += transaction["amount"]
               
                else:
                    balance -= transaction["amount"]

        
        dic["Balance"] = balance
        print(dic)


    elif menu == 4:
        for key in transHistory:
            print(key)
