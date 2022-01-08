from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from products.views import *

# app_name = 'post' 
# login_required(ProductListFilter.as_view() , login_url='login-mk')

urlpatterns = [
    path('product_list', APIProductListFilter.as_view()  , name='Product-List'),
    path('add_product_to_basket', APIAddtoBasket.as_view()  , name='Add-Product-To-Basket'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)