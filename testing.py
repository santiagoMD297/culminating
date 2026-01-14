class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the account"""
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Withdraws money if sufficient balance exists"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
          
        return 0  # No withdrawal if insufficient funds

import unittest
from bank import BankAccount  # Import the class

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Creates a new account before each test"""
        self.account = BankAccount("Alice", 100)

    def test_deposit(self):
        """Test if deposits work correctly"""
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)  # Balance should increase

        self.account.deposit(-20)  # Negative deposits should do nothing
        self.assertEqual(self.account.balance, 150)

    def test_withdraw(self):
        """Test withdrawing money"""
        amount = self.account.withdraw(40)
        self.assertEqual(amount, 40)  # Should return the withdrawn amount
        self.assertEqual(self.account.balance, 60)  # Balance should decrease

    def test_withdraw_insufficient_funds(self):
        """Test attempting to withdraw too much"""
        amount = self.account.withdraw(200)
        self.assertEqual(amount, 0)  # No money should be withdrawn
        self.assertEqual(self.account.balance, 100)  # Balance stays the same

if __name__ == '__main__':
    unittest.main()