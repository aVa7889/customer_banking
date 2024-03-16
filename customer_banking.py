# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter your savings balance: "))
    savings_interest_rate = float(input("Enter your savings interest: "))
    savings_months = int(input("Enter the length of the month for your savings: "))
    print("You have entered: ")
    print("-" * 60)
    print(f"Saving Balance: ${savings_balance:,.2f}")
    print(f"Saving Interest: ${savings_interest_rate:,.2f}")
    print(f"Saving Duration: ${savings_months}")
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, updated_savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned: ${updated_savings_interest_earned:,.2f}")  
    print(f"New savings balance: ${updated_savings_balance:,.2f}")
    print("-" * 60)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter CD initial balance: $ "))
    cd_interest_rate = float(input("Enter CD initial interest: $ "))
    cd_months = input("Enter number of months: ")
    
    if cd_months.isdigit():
            cd_months = int(cd_months)
    else:
            print("Your input is not valid.  Please try again.")
            exit()
            
    # Call the create_cd_account function and pass the variables from the user.
    new_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    
    print(f"The updated cd interest earned: ${cd_interest_earned:,.2f}")
    print(f"The updated cd balance is ${new_cd_balance:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
