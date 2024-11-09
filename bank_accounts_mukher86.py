"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 11.2.4. Bank Accounts
Date: 10/29/2024

Description:
The program simulates account transactions, including deposits, withdrawals, 
and interest accrual, printing the corresponding results after each operation.

Contributors:
    Name, login@purdue.edu [NA]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

# Main Bank Account Class Definitions
class Account:
    def __init__(self, balance):
        self.balance = balance
        print(f"New account balance: ${self.balance:.2f}")

    def deposit(self, amount):
        print(f"Deposit: ${amount:.2f}")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Withdrawal canceled.")
        else:
            print(f"Withdraw: ${amount:.2f}")
            self.balance -= amount

    def get_balance(self):
        print(f"Balance: ${self.balance:.2f}")


class Savings(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def accrue_interest(self):
        interest_payment = self.balance * self.interest_rate
        print(f"Interest payment: ${interest_payment:.2f}")
        self.balance += interest_payment


def main():
    # Start Balanced
    savings_account = Savings(200.00, 0.05)

    # Perform account activities 
    savings_account.get_balance()  
    savings_account.deposit(12.34)  
    savings_account.get_balance()  
    savings_account.withdraw(40.00)  
    savings_account.get_balance()  
    savings_account.withdraw(200.00)  
    savings_account.get_balance()  

    # Accrue interest payments
    savings_account.accrue_interest()  
    savings_account.accrue_interest()  
    savings_account.accrue_interest() 

    savings_account.withdraw(200.00)  
    savings_account.get_balance()  


if __name__ == "__main__":
    main()


