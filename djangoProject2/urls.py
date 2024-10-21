from django.contrib import admin
from django.urls import path, include

from bank.views import TransferMoneyView

urlpatterns = [
    path('bank/', include('bank.urls')),
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('transfer/', TransferMoneyView.as_view(), name='transfer_money'),
]
