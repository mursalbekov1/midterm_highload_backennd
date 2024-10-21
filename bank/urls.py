# bank/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BankCardViewSet, TransactionViewSet, RegisterView, LoginView, TransferMoneyView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bank-cards', BankCardViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('transfer/', TransferMoneyView.as_view(), name='transfer_money')

]
