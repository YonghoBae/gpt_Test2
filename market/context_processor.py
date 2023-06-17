from .models import Category
from .models import Product


def category_context(request):
    category=Category.objects.all()
    return {'category':category}


def liked_product_count(request):
    if request.user.is_authenticated:
        return {'liked_product_count': request.user.liked_products.count()}
    else:
        return {}