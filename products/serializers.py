# pip install - req

# from django.contrib.auth.models import User

from rest_framework import fields, serializers
from basket.models import Basket, BasketItem
from commentandlike.models import *

from post.models import Post
from customer.models import *
from products.models import *

# class ProductsDetailListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = '__all__'

# class CustomerListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = ['user_name']

# class CustomerDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = '__all__'

class ProductsLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_Likes
        fields = '__all__'

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ['weight']


class BasketSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Basket
        fields = '__all__'

class BasketEditSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Basket
        exclude = ['owner' , 'Chekedout_date' , 'total_products_count' , 'created_date' , 'order_date' , 'price']

class BasketItemSerializer(serializers.ModelSerializer):
    basket = BasketSerializer(read_only=True)
    class Meta:
        model = BasketItem
        exclude = [ 'added_date' , 'status']
        #depth = 1

class ShopListSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Shop
        fields = '__all__'

class CustomerSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Customer
        fields = '__all__'

class CustomerEditSerializer (serializers.ModelSerializer) :
    class Meta :
        model = Customer
        exclude = [ 'mobile' , 'date_joined' , 'username']



# class AccountSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['first_name' , 'last_name' , 'user_name'] 

# class PostSerializer(serializers.ModelSerializer):
#     customer = AccountSerializer(read_only=True)
#     class Meta:
#         model = Post
#         fields = '__all__'
#         # fields = ['id' , 'title' , 'created']
#         # depth = 1

# class PostCommentListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post_Comments
#         fields = '__all__'




    


        