transHistory = []

while True:
    try:
        menu = int(input("1. Add income""\n" "2. Add expense" "\n" "3. View balance" "\n" "4. View transaction history" "\n" "5. Quit "))
    except:
        print("Enter a number!")
        continue
    dic = {}
    

    if menu == 5:
        print("Goodbye!")
        break
    elif menu == 1:
        incomeAmount = int(input("Income amount: "))
        dic["type"] = "income"
        dic["amount"] = incomeAmount
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
