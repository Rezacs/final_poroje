import django_filters

from post.models import Post
from products.models import Products

class ProductFilters ( django_filters.FilterSet) :
    class Meta :
        model = Products
        fields = ['name' , 'created_on']