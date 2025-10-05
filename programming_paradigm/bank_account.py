class BankAccount:
    """
    A simple class to represent a bank account with deposit,
    withdraw, and balance display functionalities.
    """
    def __init__(self, initial_balance=0):
        """
        Initializes the BankAccount with an optional initial balance.

        Args:
            initial_balance (float, optional): The starting balance. Defaults to 0.
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        # Encapsulation: The account_balance is a private attribute
        # in the context of typical OOP, but in Python we use a single
        # underscore convention for protection. We'll use a standard
        # attribute name for simplicity as per the requirement:
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts the amount from the balance if funds are sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            # Funds are insufficient
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

# Example usage (for internal testing, not executed when imported):
if __name__ == "__main__":
    test_account = BankAccount(10.50)
    test_account.display_balance() # Should be $10.50

    test_account.deposit(100)
    test_account.display_balance() # Should be $110.50

    if test_account.withdraw(50):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed.")
    test_account.display_balance() # Should be $60.50

    if test_account.withdraw(200):
        print("Withdrawal successful.")
    else:
        print("Withdrawal failed (Insufficient funds).")
    test_account.display_balance() # Should be $60.50