from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from products.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# app_name = 'post' 
# login_required(ProductListFilter.as_view() , login_url='login-mk')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products', ProductList_API.as_view()  , name='Products'),
    path('add_product_to_basket', AddtoBasket_API.as_view()  , name='Add-Product-To-Basket'),
    path('basket/<int:id>/', BasketDetailUpdateDeleteView_API.as_view(), name='Basket-Detail'),
    path('shops', ShopList_API.as_view(), name='Shops'),
    path('profile/<int:id>', CustomerProfile_API.as_view(), name='Profile'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)