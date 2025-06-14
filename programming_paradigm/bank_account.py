# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        # Initialize the balance, defaulting to 0 if no initial balance is provided
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Adds the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account balance if funds are sufficient."""
        if amount > 0 and self._account_balance >= amount:
            self._account_balance -= amount
            return True
        elif amount > 0:
            print("Insufficient funds.")
        else:
            print("Withdraw amount must be positive.")
        return False

    def display_balance(self):
        """Displays the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")
