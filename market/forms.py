from django import forms
from .models import Product, Comment


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