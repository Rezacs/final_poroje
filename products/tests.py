from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from basket.models import Basket, BasketItem
from commentandlike.models import Post_Comments
from customer.models import Customer
from post.models import Post

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse
# from rest_framework.test import force_authenticate


from model_mommy import mommy

from products.models import Products, Shop

User = get_user_model()

from rest_framework import status

class Faze3TestCase (APITestCase) :

    def setUp(self):
        self.user = mommy.make(User)
        self.customer = mommy.make(Customer , mobile = self.user.mobile)
        self.user_2 = mommy.make(User)
        self.customer_2 = mommy.make(Customer , mobile = self.user_2.mobile)
        self.shop = mommy.make(Shop , status = 'chek')
        for i in range(0 , 5) :
            mommy.make(Products , shop = self.shop , quantity = i*2 )
        response = self.client.post(
            'onlineshop_api/api/token/',
            data = {
                'mobile' : self.user.mobile,
                'password' : self.user.password
            }
        )
        # self.token = response.data['access']
        # self.api_authentication()

        self.client.force_authenticate(user=self.user)
    
    def api_authentication(self) :
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer '+self.token )
    
    def test_userprofile_list_authenticated(self) :
        response = self.client.get(
            reverse('API-Profile')
        )
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_userprofile_detail_retrieve(self) :
        id = Customer.objects.get(mobile = self.user.mobile)
        #response = self.client.get(reverse('API-Profile-Edit') , kwargs = {'id' : id.pk })
        response = self.client.post(
            reverse('API-Profile-Edit' , kwargs = {'id' : id.pk } ),
            
            data = {
                'first_name' : 'test1',
                'last_name' : 'test2'
            }
        )
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_bad_userprofile_detail_retrieve(self) :
        id = Customer.objects.get(mobile = self.user.mobile)
        #response = self.client.get(reverse('API-Profile-Edit') , kwargs = {'id' : id.pk })
        response = self.client.post(
            reverse('API-Profile-Edit' , kwargs = {'id' : id.pk+1 } ),
            data = {
                'first_name' : 'test1',
                'last_name' : 'test2'
            }
        )
        self.assertNotEqual(response.status_code , status.HTTP_200_OK)

    def test_shop_list(self) :
        response = self.client.get(
            reverse('API-Shops')
        )
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_products_list(self) :
        response = self.client.get(
            reverse('API-Products')
        )
        self.assertEqual(response.status_code , status.HTTP_200_OK)

    def test_add_basket_item(self) :
        id = Customer.objects.get(mobile = self.user.mobile)
        #response = self.client.get(reverse('API-Profile-Edit') , kwargs = {'id' : id.pk })
        response = self.client.post(
            reverse('API-Basket-Item'),
            data = {
                'quantity' : '3',
                'product' : '2'
            }
        )
        self.assertEqual(response.status_code , status.HTTP_201_CREATED)

    def test_bad_add_basket_item(self) :
        id = Customer.objects.get(mobile = self.user.mobile)
        #response = self.client.get(reverse('API-Profile-Edit') , kwargs = {'id' : id.pk })
        response = self.client.post(
            reverse('API-Basket-Item'),
            data = {
                'quantity' : '1',
                'product' : '2'
            }
        )
        self.assertNotEqual(response.status_code , status.HTTP_200_OK)

    def test_edit_basket_item(self) :
        id = Customer.objects.get(mobile = self.user.mobile)
        basket = Basket.objects.get(owner = self.user)
        item = BasketItem.objects.filter(basket = basket )
        #response = self.client.get(reverse('API-Profile-Edit') , kwargs = {'id' : id.pk })
        response = self.client.post(
            reverse('API-Basket-Item-Edit' , kwargs = {'id' : item[0].pk } ),
            data = {
                'quantity' : '2',
                'product' : '2'
            }
        )
        self.assertEqual(response.status_code , status.HTTP_200_OK)












# class TestPost (APITestCase):

#     def setUp(self):
#         self.user = mommy.make(User)
#         posts = mommy.make(Post,  writer=self.user, _quantity=10)
#         comments = mommy.make(Post_Comments,  writer=self.user, _quantity=10)

#     def test_post_list(self):
#         url = reverse('seri_post_list')

#         resp = self.client.get(url)

#         self.assertEqual(resp.status_code, 200)
#         self.assertEqual(len(resp.data), 20)

#     def test_post_detailed(self):
#         for i in range (1,10) :
#             url = reverse('seri_post_detail' ,kwargs={'input_id' : i } )
#             # return redirect(reverse('delete-comment') , kwargs={'comment_id' : comment.id})
#             resp = self.client.get(url)
#             self.assertEqual(resp.status_code , 200)

#     def test_comment_list(self):
#         url = reverse('seri_comment_list')

#         resp = self.client.get(url)
        
#         self.assertEqual(resp.status_code , 200)
#         self.assertEqual(len(resp.data) , 10)

#     def test_comment_detailed(self):
#         for i in range (1,10) :
#             url = reverse('seri_comment_detail' ,kwargs={'comment_id' : i } )
#             resp = self.client.get(url)
#             self.assertEqual(resp.status_code , 200)