# Investment Accounts Assignment
import random

# Create random account list
account_list = []
for i in range(20):
    account_balance = random.randrange(0, 5000)
    account_list.append(int(account_balance))

def main():
    # Create menu loop
    done = False

    while not done:
        # Print Menu
        print ("\nMAIN MENU")
        print("1: Print Accounts")
        print("2: Deposit")
        print("3: Withdrawal")
        print("4: Count under $2000")
        print("5: Generous Donor")
        print("6: Hacker Attack")
        print("7: Exit")

        # Get selection from user
        selection = input("\nEnter Option #: ")
        if selection == "1":
            for i in range(len(account_list)):
                print("Account " + str(i) + ": $" + str(account_list[i]))
        elif selection == "2":
            print("\nDEPOSIT")
            deposit_input = input("Enter Account #: ")
            for i in range(len(account_list)):
                print("hi")
            

        elif selection == "7":
            done = True


if __name__ == "__main__":
    main()
