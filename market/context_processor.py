from .models import Category


def category_context(request):
    category=Category.objects.all()
    return {'category':category}