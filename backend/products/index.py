import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register


from .models import Product

# algoliasearch.register(Product)

@register(Product)
class ProductIndex(AlgoliaIndex):
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public'
        ]