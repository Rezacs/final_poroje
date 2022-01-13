import django_filters

from post.models import Post
from products.models import Products, Shop

class ProductFilters ( django_filters.FilterSet) :
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    shop_name = django_filters.CharFilter( field_name='shop' , lookup_expr='icontains')
    class Meta :
        model = Products
        fields = ['name' , 'created_on']

class ShopFilters ( django_filters.FilterSet) :
    class Meta :
        model = Shop
        fields = ['name' , 'created_on' , 'category' , 'type']