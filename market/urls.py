from django.urls import path

from .views import base_views, Product_views, Commet_views

app_name = 'market'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:Product_id>/', base_views.detail, name='detail'),

    # Product_views.py
    path('Product/create/', Product_views.Product_create, name='Product_create'),
    path('Product/modify/<int:Product_id>/', Product_views.Product_modify, name='Product_modify'),
    path('Product/delete/<int:Product_id>/', Product_views.Product_delete, name='Product_delete'),

    # Commet_views.py
    path('Comment/create/<int:Product_id>/', Commet_views.Comment_create, name='Comment_create'),
    path('Comment/modify/<int:Comment_id>/', Commet_views.Comment_modify, name='Comment_modify'),
    path('Comment/delete/<int:Comment_id>/', Comment_views.Comment_delete, name='Comment_delete'),
    path('Product/vote/<int:Product_id>/', Product_views.Product_vote, name='Product_vote'),
    path('vote/Comment/<int:Comment_id>/', Commet_views.Comment_vote, name='Comment_vote'),
]
