from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from commentandlike.models import Post_Comments
from customer.models import Customer
from post.models import Post

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from django.urls import reverse

from model_mommy import mommy

User = get_user_model()

from rest_framework import status

class Faze3TestCase (APITestCase) :
    profile_list_url = reverse('Profile')
    def setUp(self):
        self.user = mommy.make(User)
        response = self.client.post(
            'onlineshop_api/api/token/',
            data = {
                'mobile' : self.user.mobile,
                'password' : self.user.password
            }
        )
        self.token = response.data['access']
        self.api_authentication()
    
    def api_authentication(self) :
        self.client.credentials(HTTP_AUTHORIZATION = self.token )












class TestPost (APITestCase):

    def setUp(self):
        self.user = mommy.make(User)
        posts = mommy.make(Post,  writer=self.user, _quantity=10)
        comments = mommy.make(Post_Comments,  writer=self.user, _quantity=10)

    def test_post_list(self):
        url = reverse('seri_post_list')

        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 20)

    def test_post_detailed(self):
        for i in range (1,10) :
            url = reverse('seri_post_detail' ,kwargs={'input_id' : i } )
            # return redirect(reverse('delete-comment') , kwargs={'comment_id' : comment.id})
            resp = self.client.get(url)
            self.assertEqual(resp.status_code , 200)

    def test_comment_list(self):
        url = reverse('seri_comment_list')

        resp = self.client.get(url)
        
        self.assertEqual(resp.status_code , 200)
        self.assertEqual(len(resp.data) , 10)

    def test_comment_detailed(self):
        for i in range (1,10) :
            url = reverse('seri_comment_detail' ,kwargs={'comment_id' : i } )
            resp = self.client.get(url)
            self.assertEqual(resp.status_code , 200)