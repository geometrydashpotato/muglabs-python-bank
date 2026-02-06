# this part was so hard to make for no reason omg

money = open("saves/money.txt")
moneyContents = money.read()
moneyContents = moneyContents.strip()
currency = open("saves/currency.txt")
currencyContents = currency.read()
currencyContents = currencyContents.strip()

currency.close()
money.close()
if moneyContents == "nil":
    print("change your amount of money in saves/money.txt please!")
else:
    print(f"You have {currencyContents + moneyContents}, What would you like to do?")
    print("1. spend")
    print("2. deposit")
    choice = input(": ")
    if choice == "1":
        spent = input("how much?")
        moneyContents = int(moneyContents) - int(spent)
        with open("saves/money.txt", "w") as money:
            money.write(str(moneyContents))
    elif choice == "2":
        deposited = input("how much?")
        moneyContents = int(moneyContents) + int(deposited)
        with open("saves/money.txt", "w") as money:
            money.write(str(moneyContents))

    else:
        print("nuh uh")

    # pretty cool code huh? no? graugrlawiugldrigiguasdxhjk
