from django.test import TestCase
from .models import Product, Order, OrderItem
from bank.models import User

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=100.00,
            stock=10
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 100.00)

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.order = Order.objects.create(
            user=self.user,
            total_amount=200.00
        )

    def test_order_creation(self):
        self.assertEqual(self.order.total_amount, 200.00)
        self.assertEqual(self.order.user.username, 'testuser')

class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=100.00,
            stock=10
        )
        self.order = Order.objects.create(
            user=self.user,
            total_amount=200.00
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            price=self.product.price
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.quantity, 2)
        self.assertEqual(self.order_item.product.name, 'Test Product')