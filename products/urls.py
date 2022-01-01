from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from products.views import *

# app_name = 'post' 

urlpatterns = [
    path('dashboard', login_required(ShopDashboard.as_view() , login_url='login-mk') , name='shop-dashboard'),
    path('add_shop', login_required(AddShop.as_view() , login_url='login-mk') , name='Add_shop'),
    path('delete_shop/<int:pk>', login_required(DeleteShop.as_view() , login_url='login-mk') , name='Delete_shop'),
    path('view_shop/<int:pk>', login_required(ShopView.as_view() , login_url='login-mk') , name='Shop_Page'),
    path('edit_shop/<int:pk>', login_required(EditShop.as_view() , login_url='login-mk') , name='Edit_shop'),
    path('add_product/<int:ids>', AddProduct.as_view() , name='Add_product'),
    path('product_detail/<int:id>', class_product_detail , name='Detail_product'),
    path('delete_product_comment/<int:comment_id>',delete_product_comment,name="delete-product-comment"),
    path('edit_product/<int:pk>', EditProduct.as_view() , name='Edit_product'),
    path('edit_product_comment/<int:comment_id>', edit_comment , name='Edit_product_comment'),
    path('Shop/<str:username>', user_shop_page_view , name='Shop_Page'),
    path('add_product_comment/<int:comment_id>', add_product_comment , name='Product-comment-reply'),
    path('add_product_basket/<int:id>', add_to_basket , name='Add-Product-To-Basket'),
    path('basket', SeeBasket.as_view() , name='Basket'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)