# customer_banking

## Account_py
""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

## savings_account
"""Import the Account class from the Account.py file."""

from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # class Account:
    #    def __init__(self, balance, interest):
    #       self.balance = balance
    #       self.interest = interest
    account_instance = Account(balance, 0)

    # Calculate interest earned
    savings_interest_earned = balance * (interest_rate/100 * months/12)

    # Update the savings account balance by adding the interest earned
    updated_savings_balance = balance + savings_interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    account_instance.set_balance(updated_savings_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    account_instance.set_interest(savings_interest_earned)

    # Return the updated balance and interest earned.
    return  updated_savings_balance, savings_interest_earned
create_savings_account(1000, 10, 10)

# cd_account_py
"""Import the Account class from the Account.py file."""

from Account import Account
def create_cd_account(balance, interest_rate, months):
# def create_cd_account():
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    
    # class Account:
    #    def __init__(self, balance, interest):
    #       self.balance = balance
    #       self.interest = interest
    
    cd_account = Account(balance, 0)
    
    # Calculate interest earned
    interest_earned = balance * ((interest_rate/100) * (months/12))
    print(f"The interest earned is $: {interest_earned:,.2f}")

    # Update the CD account balance by adding the interest earned
    new_balance = balance + interest_earned
    print(f"The new balance is $ {new_balance:,.2f}")

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_account.set_balance(new_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return  new_balance, interest_earned
    
# customer_banking_py
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




