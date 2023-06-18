from django.urls import path
from .views import base_views, product_views, comment_views

app_name = 'market'

urlpatterns = [
    # base_views.py
    path('Product/list/', base_views.index, name='index'),
    path('Product/list/<str:category_name>', base_views.index, name='index'),
    path('Product/detail/<int:product_id>/', base_views.detail, name='detail'),
    
    path('', base_views.main, name='main'),
    
    # product_views.py
    path('Product/create/', product_views.Product_create, name='Product_create'),
    path('Product/modify/<int:product_id>/', product_views.Product_modify, name='Product_modify'),
    path('Product/delete/<int:product_id>/', product_views.Product_delete, name='Product_delete'),
    path('liked_products/', product_views.liked_products_view, name='liked_products'),

    # comment_views.py
    path('Comment/create/<int:product_id>/', comment_views.Comment_create, name='Comment_create'),
    path('Comment/modify/<int:comment_id>/', comment_views.Comment_modify, name='Comment_modify'),
    path('Comment/delete/<int:comment_id>/', comment_views.Comment_delete, name='Comment_delete'),
    path('Product/vote/<int:product_id>/', product_views.Product_vote, name='Product_vote'),
    path('vote/Comment/<int:comment_id>/', comment_views.Comment_vote, name='Comment_vote'),
]
