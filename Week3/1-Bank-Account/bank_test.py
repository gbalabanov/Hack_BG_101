import unittest
from bankAccount import BankAccount

class acc_test(unittest.TestCase):

    def setUp(self):
        self.my_acc=BankAccount("Gosho", 200,"BGN")

    def test_create_new_acc_instance(self):
        self.assertTrue(isinstance(self.my_acc,BankAccount))

    def test_valid_balance(self):
        self.assertEqual(self.my_acc.balance,200)

    def test_int_cast(self):
        self.assertTrue(isinstance(self.my_acc.balance,int))

    def test_str(self):
        self.assertTrue(isinstance(str(self.my_acc),str))

    def test_deposit_func(self):
        with self.assertRaises(ValueError):
            self.my_acc.deposit(-20)

    def test_withdraw_func(self):
        with self.assertRaises(ValueError):
            self.my_acc.withdraw(-20)

    def test_transfer_func(self):
        other_acc=BankAccount("Pesho",0,"BGN")
        self.assertTrue(self.my_acc.transfer_to(other_acc,200))
        self.assertEqual(other_acc.balance,200)

    def test_event_var(self):
        self.assertIsInstance(self.my_acc.events,list)








if __name__ == '__main__':
    unittest.main()
