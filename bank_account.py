#!/usr/bin/env python3

from datetime import datetime


class BankAccount:

    def __init__(self, account_number, holder_name, initial_balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = initial_balance
        self.transaction_history = []

        # Record account creation
        self._record_transaction("Account Created", initial_balance)

    def _record_transaction(self, transaction_type, amount):
        """Private helper method to store transaction details."""
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        self._record_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        self._record_transaction("Withdraw", amount)

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        target_account.balance += amount

        self._record_transaction("Transfer Sent", amount)
        target_account._record_transaction("Transfer Received", amount)

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] | Holder: {self.holder_name} | Balance: {self.balance}"

    def show_transaction_history(self):
        print(f"\nTransaction History for {self.holder_name}:")
        for txn in self.transaction_history:
            print(f"{txn['timestamp']} | {txn['type']} | Amount: {txn['amount']}")


if __name__ == "__main__":
    acc1 = BankAccount("1001", "Alice", 1000)
    acc2 = BankAccount("1002", "Bob", 500)

    acc1.deposit(200)
    acc1.withdraw(150)
    acc1.transfer(300, acc2)

    print(acc1)
    print(acc2)

    acc1.show_transaction_history()
    acc2.show_transaction_history()
