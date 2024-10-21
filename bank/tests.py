# bank/tests.py
from django.test import TestCase
from .models import User, BankCard, Transaction

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            phone_number='1234567890',
            location='Test Location',
            account_id='acc123',
            card_id='card123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.phone_number, '1234567890')

class BankCardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            phone_number='1234567890',
            location='Test Location',
            account_id='acc123',
            card_id='card123'
        )
        self.bank_card = BankCard.objects.create(
            user=self.user,
            card_number='1234567890123456',
            cvv='123',
            expiry_date='2025-12-31'
        )

    def test_bank_card_creation(self):
        self.assertEqual(self.bank_card.user, self.user)
        self.assertEqual(self.bank_card.card_number, '1234567890123456')

    def test_str_method(self):
        self.assertEqual(str(self.bank_card), 'Card ending with 3456')

class TransactionModelTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(
            username='sender',
            password='testpassword'
        )
        self.receiver = User.objects.create_user(
            username='receiver',
            password='testpassword'
        )
        self.transaction = Transaction.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            amount=100.00,
            description='Payment for services'
        )

    def test_transaction_creation(self):
        self.assertEqual(self.transaction.sender, self.sender)
        self.assertEqual(self.transaction.receiver, self.receiver)
        self.assertEqual(self.transaction.amount, 100.00)

    def test_str_method(self):
        self.assertIn('Transaction of 100.00 from', str(self.transaction))
