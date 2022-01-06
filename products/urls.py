from django.contrib import admin
from django.urls import path , include
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from products.views import *

# app_name = 'post' 

urlpatterns = [
    path('dashboard', login_required(ShopDashboard.as_view() , login_url='login-mk') , name='shop-dashboard'),
    path('useless_shops', login_required(UseLessShopDashboard.as_view() , login_url='login-mk') , name='Useless-Shops'),
    path('add_shop', login_required(AddShop.as_view() , login_url='login-mk') , name='Add_shop'),
    path('delete_shop/<int:pk>', login_required(DeleteShop.as_view() , login_url='login-mk') , name='Delete_shop'),
    path('view_shop/<int:pk>', login_required(ShopView.as_view() , login_url='login-mk') , name='Shop_Page'),
    path('edit_shop/<int:pk>', login_required(EditShop.as_view() , login_url='login-mk') , name='Edit_shop'),
    path('add_product/<int:ids>', login_required(AddProduct.as_view() , login_url='login-mk') , name='Add_product'),
    path('product_detail/<int:id>', class_product_detail , name='Detail_product'),
    path('delete_product_comment/<int:pk>',login_required(DeleteProductComment.as_view() , login_url='login-mk'),name="delete-product-comment"),
    path('edit_product/<int:pk>', EditProduct.as_view() , name='Edit_product'),
    path('edit_product_comment/<int:pk>', login_required(EditProductComment.as_view() , login_url='login-mk') , name='Edit_product_comment'),
    path('Shop/<str:username>', login_required(UserShopsView.as_view() , login_url='login-mk') , name='Shop_Page'),
    path('add_images/<int:pk>', login_required(FileFieldFormView.as_view() , login_url='login-mk') , name='Add-Product-Images'),
    path('add_product_comment/<int:comment_id>', add_product_comment , name='Product-comment-reply'),
    path('add_product_basket/<int:id>', add_to_basket , name='Add-Product-To-Basket'),
    path('basket', basket , name='Basket'),
    path('edit_basket/<int:pk>', edit_basket , name='Edit-Basket'),
    path('delete_from_basket/<int:pk>', delete_product_from_basket , name='Delete-From-Basket'),
    path('pay_baset/<int:pk>', checkout_basket , name='Pay-Basket'),
    path('shop_statistics/<int:pk>', login_required(ShopStatistics.as_view() , login_url='login-mk') , name='Statistics'),
    path('edit_item_status/<int:pk>', edit_baskeitem_status , name='Edit-Item-Status'),
    path('edit_basket_item_quantity/<int:pk>', edit_basket_item_quantity , name='Edit-Basket-Item-Quantity'),
    path('restore_shop/<int:pk>', restore_shop , name='Restore-Shop'),
    path('product_liked_detail/<int:pk>', product_liked_details , name='Product-Like-Detail'),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)