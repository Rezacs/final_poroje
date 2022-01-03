from django.shortcuts import render
from django.views.generic import *
from basket.models import Basket
from commentandlike.models import *
from customer.models import *
from products.models import *
from products.serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.serializers import *
from products.forms import *
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseNotFound
from basket.models import *

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()



@api_view(['GET'])
def products_list_2(request):

    products = Products.objects.all()

    serializer = ProductsListSerializer(products , many=True)

    return Response(data = serializer.data , status=200)
@api_view(['GET'])
def products_detail_2(request , input_id):

    products = Products.objects.get(id = input_id)

    serializer = PostSerializer(products)

    return Response(data = serializer.data , status=200)
@api_view(['GET'])
def products_likes(request , input_id):

    #post = Post.objects.get(id = input_id)
    product_like = Products_Likes.objects.filter(products__id = input_id )

    serializer = ProductsLikeSerializer(product_like)

    return Response(data = serializer.data , status=200)
@api_view(['GET'])
def post_comments_list_2(request):

    comments = Post_Comments.objects.all()

    serializer = PostCommentListSerializer(comments , many = True)

    return Response(data = serializer.data , status=200)
@api_view(['GET'])
def post_comments_detail_2(request , comment_id):

    comments = Post_Comments.objects.filter(id = comment_id).all()

    serializer = PostCommentListSerializer(comments , many = True)

    return Response(data = serializer.data , status=200)

#FINAL_PROJECT

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


#@permission_classes([IsAuthenticated])
#from django.utils.decorators import method_decorator
#@method_decorator(login_required, name='dispatch')
class ShopDashboard (ListView):
    model = Shop
    context_object_name = 'shops'
    template_name = 'set_shop/dashboard.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner = self.request.user)
    def get_context_data(self, **kwargs):
        context = super(ShopDashboard, self).get_context_data(**kwargs)
        user = self.request.user
        shops = Shop.not_deleted.filter(owner = user)
        customer = Customer.objects.get(mobile=user.mobile)
        followers = UserConnections.objects.filter(follower=user)
        followings = UserConnections.objects.filter(following=user)
        context.update({
            'user' : user,
            'customer':customer,
            'followers':followers,
            'followings':followings,
        })
        return context

@login_required(login_url='login-mk')
def shop_dashboard ( request ) :
    user = request.user
    shops = Shop.not_deleted.filter(owner = user)
    customer = Customer.objects.get(mobile=user.mobile)
    followers = UserConnections.objects.filter(follower=user)
    followings = UserConnections.objects.filter(following=user)
    return render ( request , 'set_shop/dashboard.html' , {
        'shops' :shops,
        'user' : user,
        'customer':customer,
        'followers':followers,
        'followings':followings,
    })

class AddShop(CreateView):
    model = Shop
    #fields = ['name']
    form_class = AddShopForm
    #exclude = ['shop']
    #form = AddProductForm()
    template_name = 'set_shop/shop_form.html'
    success_url = '/dashboard'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.customer= Customer.objects.get(mobile = self.request.user.mobile)
        self.object.save()
        return redirect(reverse('shop-dashboard'))

def add_Shop ( request ) :
    form = AddShopForm(request.POST or None )
    if request.method == "POST" :
        if form.is_valid() :
            # ['status' , 'owner' , 'customer' , 'admin_description' , 'created_on']
            shop = form.save(commit=False)
            shop.status = 'load'
            shop.owner = request.user
            shop.customer= Customer.objects.get(user_name = request.user.username)
            shop.save()
            messages.add_message(request, messages.SUCCESS, 'shop was saved !')
            return redirect(reverse('shop-dashboard'))
    return render(request,'set_shop/shop_form.html' ,{
        'form' : form
    })

class DeleteShop(DeleteView):
    model = Shop
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user == self.object.owner :    
            self.object.status = 'dele'
            self.object.save()
            messages.add_message(request, messages.SUCCESS, 'shop was deleted !')
            return redirect('/onlineshop/dashboard')
        else :
            return HttpResponse('you dont have permission to do this !')

def delete_shop(request,id):
    shop = get_object_or_404(Shop ,id=id)
    if request.user == shop.owner :    
        shop.status = 'dele'
        shop.save()
        messages.add_message(request, messages.SUCCESS, 'shop was deleted !')
        return redirect('/onlineshop/dashboard')
    else :
        return HttpResponse('you dont have permission to do this !')

#mixin_dispatch
class EditShop(UpdateView):
    model = Shop
    form_class = AddShopForm
    template_name = 'set_shop/edit_shop.html'
    context_object_name = 'specified_post'
    #success_url = redirect(f'/onlineshop/view_shop/{get_object().id}')
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user == self.object.owner :    
            self.object.save()
            messages.add_message(request, messages.SUCCESS, 'shop was edited !')
            return redirect(f'/onlineshop/view_shop/{self.get_object().id }')
        else :
            return HttpResponse('you dont have permission to do this !')

    def get_success_url(self):
        return reverse('Shop_Page', kwargs={'pk': self.get_object().id})

def edit_shop ( request , id ) :
    specified_shop = get_object_or_404(Shop , id =id )
    form = AddShopForm(instance=specified_shop)
    if request.method == "POST" :
        if request.user == specified_shop.owner :
            form = AddShopForm(request.POST , request.FILES , instance=specified_shop)
            if form.is_valid() :
                bad_shop = form.save(commit=False)
                bad_shop.status = 'load'
                form.save_m2m()
                bad_shop.save()
                messages.add_message(request, messages.SUCCESS, 'shop was edited !')
                return redirect(f'/onlineshop/view_shop/{id}')
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'set_shop/edit_shop.html',{'form' : form , 'specified_post' : specified_shop})

class AddProduct(View):
    def get(self, request, *args, **kwargs):
        self.object = None
        shop = Shop.accepted.filter(id = self.kwargs['ids'] )
        print('gggggggggggggggggggggg' , shop , '  -  ' , shop.first().id )
        if not shop : 
            messages.add_message(request, messages.WARNING , 'your shop is not verified !')
            return redirect(f"/onlineshop/view_shop/{self.kwargs['ids'] }")
        form = AddProductForm(None or self.request.POST , self.request.FILES , shop.first().id)
        return render (request , 'set_shop/new_product.html' , {'form' : form , 'shop' : shop})

    def post(self, request, *args, **kwargs):
        self.object = None
        shop = Shop.accepted.filter(id = self.kwargs['ids'] )
        form = AddProductForm(None or self.request.POST , self.request.FILES ,  shop.first().id)
        bad_product = form.save(commit=False)
        bad_product.shop = shop[0]  #request.user
        bad_product.save()
        messages.add_message(request, messages.INFO , 'new product was saved !')
        return redirect(f'/onlineshop/view_shop/{shop[0].id }')

def add_product (request , ids ) :
    form = AddProductForm(None or request.POST , request.FILES)
    shop = Shop.accepted.filter(id = ids )
    if not shop : 
        messages.add_message(request, messages.WARNING , 'your shop is not verified !')
        return redirect(f'/onlineshop/view_shop/{ids }')
    if request.method == "POST" :
        if form.is_valid() :
            bad_product = form.save(commit=False)
            bad_product.shop = shop[0]  #request.user
            bad_product.save()
            messages.add_message(request, messages.INFO , 'new product was saved !')
            return redirect(f'/onlineshop/view_shop/{ids }')
            # return redirect(reverse('shop-dashboard'))

    return render (request , 'set_shop/new_product.html' , {'form' : form , 'shop' : shop})

def class_product_detail ( request , id ) : 
    product = Products.objects.get(id = id)
    user = request.user
    likes = Products_Likes.objects.filter(products__id = id )
    if user.is_authenticated :
        customer = Customer.objects.get(mobile =user.mobile)
        check_like_product = Products_Likes.objects.filter(products = product).filter(writer = user)
        check_like_comment = Products_Comment_likes.objects.filter(comments__products = product).filter(writer = user)
    else :
        customer = Customer.objects.get(user_name ='Anonymous')
        check_like_product = False
        check_like_comment = False
    form = ProductCommentModelForm()
    form2 = LikeProductForm()
    form3 = LikeProductCommentForm()
    comments = Products_Comments.objects.filter(products = product)
    if request.method == "POST" :
        if 'form' in request.POST :
            form = ProductCommentModelForm(request.POST) # validate
            if form.is_valid() :
                print(form.cleaned_data)
                comment = form.save(commit=False)
                comment.products = product
                comment.customer = customer
                comment.writer= user
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'comment was saved !')

        if 'form2' in request.POST :
            form2 = LikeProductForm(request.POST)
            if form2.is_valid() :
                if check_like_product :
                    check_like_product.delete()
                else :
                    like = form2.save(commit=False)
                    like.writer = user
                    like.products = product
                    like.save()

        return redirect(f'/onlineshop/product_detail/{product.id}')

    return render(request , 'set_shop/class_product_detail.html', {
        'product' : product ,
        'comments' : comments ,
        'form' : form,
        'user' : user ,
        'likes' : likes ,
        'form2' : form2 ,
        'check_like_post' : check_like_product ,
        'check_like_comment' : check_like_comment ,
        'form3' : form3
    })

class DeleteProductComment(DeleteView):
    model = Products_Comments
    template_name = 'set_shop/delete_comment.html'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(DeleteProductComment, self).get_object()
        if not obj.writer == self.request.user:
            return HttpResponse('you dont have permission to do this !')
        return obj
    def get_success_url(self):
        return reverse('Detail_product', kwargs={'id': self.get_object().products.id})

def delete_product_comment(request,pk):
    
    comment = get_object_or_404(Products_Comments,id=pk)
    if request.user == comment.writer :    
        comment.delete()
        product = comment.products
        messages.add_message(request, messages.SUCCESS, 'comment was deleted !')
        return redirect(f'/onlineshop/product_detail/{product.id}')
    else :
        return HttpResponse('you dont have permission to do this !')

class EditProduct(UpdateView):
    model = Products
    #fields = ['name']
    form_class = AddProductForm
    #exclude = ['shop']
    #form = AddProductForm()
    template_name = 'set_shop/edit_product.html'
    #success_url = f'/onlineshop/product_detail/{pk}'

    def post(self, request, *args, **kwargs):
        shop = Shop.accepted.filter(id = self.kwargs['pk'] )
        messages.add_message(request, messages.SUCCESS, 'product was edited !')
        return redirect(f'/onlineshop/view_shop/{shop[0].id }')
    
def edit_product ( request , id ) :
    specified_product = get_object_or_404(Products , id =id )
    form = AddProductForm(instance=specified_product)
    if request.method == "POST" :
        if request.user == specified_product.shop.owner :
            form = AddProductForm(request.POST , request.FILES , instance=specified_product)
            if form.is_valid() :
                form.save(commit=False)
                form.save_m2m()
                form.save()
                messages.add_message(request, messages.SUCCESS, 'product was edited !')
                return redirect(f'/onlineshop/product_detail/{specified_product.id}')
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'set_shop/edit_product.html',{'form' : form , 'specified_post' : specified_product})

class EditProductComment (UpdateView):
    model = Products_Comments
    form_class = ProductCommentModelForm
    template_name = 'set_shop/edit_comment.html'
    #success_url = f'/onlineshop/product_detail/{pk}'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EditProductComment, self).get_object()
        if not obj.writer == self.request.user:
            return HttpResponse('you dont have permission to do this !')
        return obj
    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS, 'product was edited !')
        return reverse('Detail_product', kwargs={'id': self.get_object().products.id})

def edit_comment ( request , id ) :
    comment = get_object_or_404(Products_Comments , id =id )
    product = comment.products
    # print(request.user)
    # print(request.user.email)
    form = ProductCommentModelForm(instance=comment)
    if request.method == "POST" :
        if request.user == comment.writer : 
            form = ProductCommentModelForm(request.POST , instance=comment)
            if form.is_valid() :
                form.save()
                messages.add_message(request, messages.SUCCESS , 'commment was edited !')
                return redirect(f'/onlineshop/product_detail/{product.id}')
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'set_shop/edit_comment.html',{'form' : form , 'comment' : comment , 'product' : product})

def add_product_comment ( request , comment_id ) :
    comment = get_object_or_404(Products_Comments , id =comment_id )
    product = comment.products
    user = request.user
    customer = Customer.objects.get(user_name =user.username)
    form = ProductCommentModelForm()
    if request.method == "POST" :
        form = ProductCommentModelForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit=False)
            comment.products = product
            comment.customer = customer
            comment.writer= user
            comment.parent = Products_Comments.objects.get(id = comment_id)
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'comment was saved !')
            return redirect(f'/onlineshop/product_detail/{product.id}')

    return render ( request , 'set_shop/add_comment.html' , {'form' : form , 'post' : product} )

class UserShopsView (ListView):
    model = Shop
    context_object_name = 'shops'
    template_name = 'set_shop/user_shops_view.html'
    def get_queryset(self):
        pointed_user = User.objects.get(username = self.kwargs['username'])
        queryset = super().get_queryset()
        return queryset.filter(owner = pointed_user)
    def get_context_data(self, **kwargs):
        context = super(UserShopsView, self).get_context_data(**kwargs)
        user = self.request.user
        #shops = Shop.not_deleted.filter(owner = user)
        customer = Customer.objects.get(mobile=user.mobile)
        followers = UserConnections.objects.filter(follower=user)
        followings = UserConnections.objects.filter(following=user)
        context.update({
            'user' : user,
            'customer':customer,
            'followers':followers,
            'followings':followings,
        })
        return context

def user_shop_page_view ( request , username ) :
    pointed_user = User.objects.get(username = username)
    shops = Shop.accepted.filter(owner = pointed_user)
    customer = Customer.objects.get(user_name=username)
    followers = UserConnections.objects.filter(follower=pointed_user)
    followings = UserConnections.objects.filter(following=pointed_user)

    return render ( request , 'set_shop/user_shops_view.html' , {
        'shops' :shops,
        'pointed_user' : pointed_user,
        'customer':customer,
        'followers':followers,
        'followings':followings,
    })

def add_to_basket (request , id ) :
    product = Products.objects.get ( id = id )
    if product.quantity < 1 or product.shop.status != 'chek' :
        messages.add_message(request, messages.SUCCESS, 'not enough left for you - or shop is banned !')
        return redirect(f'/onlineshop/product_detail/{product.id}')
    basket = Basket.objects.filter(owner = request.user).filter(status = 'live')
    if basket :
        item = BasketItem.objects.filter(product=product).filter(basket = basket[0])
        if item :
            item[0].quantity += 1
            messages.add_message(request, messages.SUCCESS , 'product is already in your basket !')
            return redirect(f'/onlineshop/product_detail/{product.id}')
        else :
            BasketItem.objects.create(product=product , quantity = 1 , basket = basket[0])
    else :
        trash = Basket.objects.create(owner = request.user , status='live' )
        BasketItem.objects.create(product=product , quantity = 1 , basket = trash)

    messages.add_message(request, messages.SUCCESS , 'product added to basket !')
    return redirect(f'/onlineshop/product_detail/{product.id}')

class SeeBasket(View):
    model = Shop
    template_name = 'set_shop/new_product.html'
    form_class = AddShopForm
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(AddProduct, self).get_object()
        if not obj.owner == self.request.user:
            return HttpResponse('you dont have permission to do this !')
        if not obj.status == 'chek' :
            messages.add_message(self.request, messages.WARNING , 'your shop is not verified !')
            return redirect(f'/onlineshop/view_shop/{self.get_object().shop.id }')
        return obj
    def get_success_url(self):
        return reverse('Detail_product', kwargs={'id': self.get_object().products.id})

class ShopView (DetailView):
    model = Shop
    context_object_name = 'post'
    template_name = 'set_shop/Shop_view.html'
    def get_context_data(self, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        self.object = self.get_object()
        products = Products.objects.filter (shop = self.object)
        context.update({
            'products' : products,
        })
        return context

def shop_owner_view ( request , id) :
    user = request.user
    shop = Shop.objects.get(id = id)
    products = Products.objects.filter (shop = shop)
    return render ( request , 'set_shop/Shop_view.html' , {
        'post' :shop,
        'products' : products,
    })

@login_required(login_url='login-mk')
def basket ( request ) :
    user = request.user
    baskets = Basket.objects.filter(owner = user)
    live = Basket.objects.filter(status = 'live')
    items = BasketItem.objects.filter(basket__in=baskets)
    live_items = items.filter(basket__status='live')

    customer = Customer.objects.get(user_name=user.username)
    return render ( request , 'baskets.html' , {
        'baskets' :baskets,
        'user' : user,
        'customer':customer,
        'items' : items,
        'live' : live,
        'live_items' : live_items
    })
@login_required(login_url='login-mk')
def edit_basket ( request , pk ) :
    basket = get_object_or_404(Basket , id =pk )
    form = BasketAddressForm(instance=basket)
    if request.method == "POST" :
        if request.user == basket.owner : 
            form = BasketAddressForm(request.POST , instance=basket)
            if form.is_valid() :
                form.save()
                messages.add_message(request, messages.SUCCESS , 'changes submited !')
                return redirect('/onlineshop/basket')
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'set_shop/edit_comment.html',{'form' : form  , 'basket' : basket})
@login_required(login_url='login-mk')
def delete_product_from_basket(request,pk):
    
    product = get_object_or_404(Products,id=pk)
    basket = Basket.objects.get(owner = request.user , status='live')
    qry = BasketItem.objects.filter(basket = basket ).filter(product=product)
    qry.delete()
    messages.add_message(request, messages.SUCCESS, 'product was removed from basket !')
    return redirect('/onlineshop/basket')
@login_required(login_url='login-mk')
def checkout_basket ( request , pk ) :
    basket = get_object_or_404(Basket,id=pk)
    basket.status = 'past'
    messages.add_message(request, messages.SUCCESS, 'basket payed !')
    products = BasketItem.objects.filter(basket = basket)
    for p in products :
        p.product.quantity -= p.quantity
    return redirect('/onlineshop/basket')

@login_required(login_url='login-mk')
def shop_statistics ( request , pk ) :
    shop = get_object_or_404(Shop,id=pk)
    if request.user != shop.owner :
        return HttpResponse('you dont have permission to do this !')
    sells = BasketItem.objects.filter( product__shop = shop).order_by('-added_date')
    products = Products.objects.filter(shop = shop)
    user = request.user
    likes = Products_Likes.objects.filter(products__in=products)
    form = SelledItemsForm(request.POST, prefix="sells")
    # form2 = LikeProductForm()
    # form3 = LikeProductCommentForm()
    if request.method == "POST" :
        if 'form' in request.POST :
            form = SelledItemsForm(request.POST) # validate
            if form.is_valid() :
                print(form.cleaned_data)
                comment = form.save(commit=False)
                comment.save()
                messages.add_message(request, messages.SUCCESS, 'changes submited !')

    #     if 'form2' in request.POST :
    #         form2 = LikeProductForm(request.POST)
    #         if form2.is_valid() :
    #             if check_like_product :
    #                 check_like_product.delete()
    #             else :
    #                 like = form2.save(commit=False)
    #                 like.writer = user
    #                 like.products = product
    #                 like.save()

        return redirect(f'/onlineshop/shop_statistics/{shop.id}')

    return render(request , 'set_shop/statistics.html', {
        'post' :shop,
        'sells' : sells,
        'products' : products ,
        'form' : form,
        'user' : user ,
        'likes' : likes ,
    })


def edit_baskeitem_status ( request , pk ) :
    item = get_object_or_404(BasketItem , id=pk )
    buyer = item.basket.owner
    form = SelledItemsForm(instance=item)
    if request.method == "POST" :
        if request.user == item.product.shop.owner : 
            form = SelledItemsForm(request.POST , instance=item)
            if form.is_valid() :
                form.save()
                messages.add_message(request, messages.SUCCESS , 'status changed !')
                return redirect(f'/onlineshop/shop_statistics/{item.product.shop.id}')
        else :
            return HttpResponse('you dont have permission to do this !')
    return render ( request , 'set_shop/edit_basket_item_status.html',{'form' : form , 'buyer' : buyer})