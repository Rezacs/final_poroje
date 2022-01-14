from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.urls.conf import re_path
from django.views.generic import TemplateView
from products.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf.urls import url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# app_name = 'post' 
# login_required(ProductListFilter.as_view() , login_url='login-mk')

# login_required(ShopDashboard.as_view() , login_url='login-mk')
# 

urlpatterns = [
    path('register', RegisterUser_API.as_view() , name='API-Register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile', CustomerProfileList_API.as_view() , name='API-Profile'),
    path('profile/<int:id>', CustomerProfile_API.as_view() , name='API-Profile-Edit'),
    path('shops', ShopList_API.as_view(), name='API-Shops'),
    path('products', ProductList_API.as_view()  , name='API-Products'),
    path('basket_item', AddtoBasket_API.as_view()  , name='API-Basket-Item'),
    path('basket_item/<int:id>', BasketItemUpdateDeleteView_API.as_view() , name='API-Basket-Item-Edit'),
    path('basket', Baskets_API.as_view()  , name='API-Basket'),
    path('basket/<int:id>/', BasketDetailUpdateDeleteView_API.as_view(), name='API-Basket-edit'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)