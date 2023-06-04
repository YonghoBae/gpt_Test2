from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Comment, CustomUser


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # 사용할 모델
        fields = ['name', 'content', 'image', 'price']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'name': '제목',
            'content': '내용',
            'image': '이미지',
            'price': '가격',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글',
        }


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "email", "address"]