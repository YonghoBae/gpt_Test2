from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Product, Comment, Category, Profile


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ProfileInline(admin.StackedInline):
    model=Profile
    con_delete=False

class CustomUserAdmin(UserAdmin):
    inlines=(ProfileInline,)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)

# 기존의 User의 등록을 취소했다가 User와 ProfileInline을 붙임.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)