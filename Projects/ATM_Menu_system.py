balance = 1500

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawl")
    print("4. Exit")

    Choice = input("Choose an option: ")

    if Choice == "1":
        print(f"Your balance: {balance}$")
    elif Choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print(f"Deposited ${amount}")
    elif Choice == "3":
        amount = float(input("Enter withdrawl amount: "))
        if amount <= balance:
            balance -= amount   
            print(f"Withdrew {amount}$")
        else:
            print("Insufficient fund!")

    elif Choice == "4":
        print("Thank you for using ATM!")
        break
    else:
        print("Invalid Option!")
