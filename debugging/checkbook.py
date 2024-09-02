class Checkbook:
    """
    A simple Checkbook class to manage a bank account with basic operations
    such as deposit, withdraw, and check balance.
    """

    def __init__(self):
        """
        Initializes a Checkbook instance with a balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook account.

        Parameters:
        amount (float): The amount of money to deposit. Should be a positive value.

        Returns:
        None

        Side Effects:
        Prints a message confirming the deposit and the updated balance.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook account.

        Parameters:
        amount (float): The amount of money to withdraw. Should be a positive value.

        Returns:
        None

        Side Effects:
        Prints a message confirming the withdrawal and the updated balance.
        If the withdrawal amount exceeds the current balance, an error message is printed.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook account.

        Parameters:
        None

        Returns:
        None

        Side Effects:
        Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Prompts the user for a valid amount and returns it as a float.

    Parameters:
    prompt (str): The prompt message to display to the user.

    Returns:
    float: The valid amount entered by the user.

    Raises:
    ValueError: If the user input cannot be converted to a float.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("The amount must be positive.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def main():
    """
    Main function to interact with the Checkbook class.
    
    Provides a command-line interface for the user to perform operations:
    deposit, withdraw, check balance, and exit the program.
    
    Parameters:
    None

    Returns:
    None

    Side Effects:
    Prints messages to the console based on user actions.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
