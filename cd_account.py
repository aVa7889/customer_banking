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
# create_cd_account(2000, 10, 10)


