import unittest
import expensetracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        global expenses
        expenses = []
    
    def test_add_expense(self):
        date = "2025-02-25"
        description = "Groceries"
        amount = 100.0
        expenses.append({'date': date, 'description': description, 'amount': amount})
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]['date'], date)
        self.assertEqual(expenses[0]['description'], description)
        self.assertEqual(expenses[0]['amount'], amount)
    
    def test_view_expenses(self):
        date = "2025-02-25"
        description = "Groceries"
        amount = 100.0
        expenses.append({'date': date, 'description': description, 'amount': amount})
        expected = [{'date': "2025-02-25", 'description': "Groceries", 'amount': 100.0}]
        self.assertEqual(expenses, expected)
    
    def test_calculate_expenses(self):
        expenses.append({'date': "2025-02-25", 'description': "Groceries", 'amount': 100.0})
        expenses.append({'date': "2025-02-26", 'description': "Books", 'amount': 50.0})
        expected = 150.0
        total = sum(expense['amount'] for expense in expenses)
        self.assertEqual(total, expected)

if __name__ == '__main__':
    unittest.main()
