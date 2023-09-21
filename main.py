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
                print(f"Account {str(i)}: ${str(account_list[i])}")
        # Deposit Option
        elif selection == "2":
            print("\nDEPOSIT")
            deposit_account_input = input("Enter Account #: ")
            for i in range(len(account_list)):    
                if deposit_account_input == str(i):            
                    deposit_amount = input("Enter amount to deposit: $")
                    new_balance_after_deposit = account_list[i] + int(deposit_amount)
                    print (f"Account {str(i)} Previous Balance: ${str(account_list[i])}")
                    print (f"Account {str(i)} New Balance: ${str(new_balance_after_deposit)}")
                    account_list[i] = new_balance_after_deposit
        # Withdrawal Option
        elif selection == "3":
            print("\nWITHDRAWAL")
            withdrawal_account_input = input("Enter Account #: ")
            for i in range(len(account_list)):
                if withdrawal_account_input == str(i):
                    withdrawal_amount = input("Enter amount to withdraw: $")
                    new_balance_after_withdrawal = account_list[i] - int(withdrawal_amount)
                    if new_balance_after_withdrawal < 0:
                        print("Sorry, insuffiecient funds.")
                    else:
                        print(f"Account {str(i)} Previous Balance: ${str(account_list[i])}")
                        print(f"Account {str(i)} New Balance: ${str(new_balance_after_withdrawal)}")
                        account_list[i] = new_balance_after_withdrawal
        # Count Under $2000
        elif selection == "4":
            print("\nCOUNT UNDER $2000")
            under_2000_count = 0
            for i in range(len(account_list)):
                if account_list[i] < 2000:
                    under_2000_count += 1
                    print(f"Account {str(i)}: ${account_list[i]}")
                    print(f"Accounts with less than $2000: {str(under_2000_count)}")
        # Generous Donor
        elif selection =="5":
            print("GENEROUS DONOR")
            accounts_donated_count = 0
            total_amount_donated = 0
            for i in range(len(account_list)):
                if account_list[i] < 2000:
                    accounts_donated_count += 1
                    total_amount_donated += 500
                    new_balance_after_donor = account_list[i] + 500
                    print(f"Account {str(i)} Previous Balance: ${str(account_list[i])}")
                    print(f"Account {str(i)} New Balance: ${str(new_balance_after_donor)}")
                    account_list[i] += 500
            print(f"Number of accounts donated to {accounts_donated_count}, Total amount donated ${total_amount_donated}")
        # Hacker Attack
        elif selection == "6":
            print("HACKER ATTACK")
            total_amount_stolen = 0
            for i in range(len(account_list)):
                total_amount_stolen += account_list[i] * 0.05
                account_list[i] = account_list[i] - account_list[i] * 0.05
            print(f"Total stolen is: ${total_amount_stolen}")
        # Exit
        elif selection == "7":
            done = True


if __name__ == "__main__":
    main()
