import unittest
from AccountValidation import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Matthew", initial_balance = 500)

    def test_get_menu(self):
        menu = self.account.get_menu()
        expected_menu = """
        1 Deposit
        2 Withdraw
        """
        self.assertEqual(menu, expected_menu)

    def test_get_name(self):
        self.assertEqual(self.account.get_name(), "Matthew")

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 500)
        self.assertEqual(self.account.name, "Matthew")

    def test_deposit(self):
        result = self.account.deposit(100)
        self.assertEqual(result, 600)  
        self.assertEqual(self.account.balance, 600)

    def test_withdraw_success(self):
        result = self.account.withdraw(200)
        self.assertEqual(result, 300) 
        self.assertEqual(self.account.balance, 300)

    def test_withdraw_insufficient_funds(self):
        result = self.account.withdraw(600)
        self.assertEqual(result, "Insufficient funds")
        self.assertEqual(self.account.balance, 500)  # Ensure balance is not updated

    def test_get_menu(self):
        menu = self.account.get_menu()
        expected_menu = """
        1 Deposit
        2 Withdraw
        """
        self.assertEqual(menu.strip(), expected_menu.strip())

if __name__ == "__main__":
    unittest.main()
