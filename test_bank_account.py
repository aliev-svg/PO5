
import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # Создаётся перед каждым тестом.
        self.account = BankAccount("Alu", "12345")
        self.second_account = BankAccount("Ali", "67890")

    def test_create_account(self):
        self.assertEqual(self.account.owner, "Alu")
        self.assertEqual(self.account.account_number, "12345")
        self.assertEqual(self.account.get_balance(), 0.0)

    def test_invalid_account_data(self):
        with self.assertRaises(ValueError):
            BankAccount("", "12345")

        with self.assertRaises(ValueError):
            BankAccount("Alu", "")

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 500)

    def test_deposit_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

        with self.assertRaises(ValueError):
            self.account.deposit(0)

        with self.assertRaises(ValueError):
            self.account.deposit("abc")

    def test_withdraw(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 300)

    def test_withdraw_more_than_balance(self):
        self.account.deposit(100)

        with self.assertRaises(ValueError):
            self.account.withdraw(200)

        # Баланс не должен измениться.
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw_invalid_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    def test_transfer(self):
        self.account.deposit(500)
        self.account.transfer(self.second_account, 200)

        self.assertEqual(self.account.get_balance(), 300)
        self.assertEqual(self.second_account.get_balance(), 200)

    def test_transfer_more_than_balance(self):
        self.account.deposit(100)

        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, 200)

        # Оба счёта должны остаться без изменений.
        self.assertEqual(self.account.get_balance(), 100)
        self.assertEqual(self.second_account.get_balance(), 0)

    def test_transfer_to_self(self):
        self.account.deposit(100)

        with self.assertRaises(ValueError):
            self.account.transfer(self.account, 50)

        self.assertEqual(self.account.get_balance(), 100)

    def test_transfer_invalid_amount(self):
        self.account.deposit(100)

        with self.assertRaises(ValueError):
            self.account.transfer(self.second_account, -10)

        self.assertEqual(self.account.get_balance(), 100)
        self.assertEqual(self.second_account.get_balance(), 0)

    def test_get_balance_after_operations(self):
        self.account.deposit(1000)
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_is_empty(self):
        self.assertTrue(self.account.is_empty())

        self.account.deposit(100)
        self.assertFalse(self.account.is_empty())

        self.account.withdraw(100)
        self.assertTrue(self.account.is_empty())


if __name__ == "__main__":
    unittest.main()
