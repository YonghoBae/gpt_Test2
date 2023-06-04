from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20,unique=True)
    description=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('market:index',args=[self.name])


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default='', related_name='author_question')
    name = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    view_count = models.IntegerField(default=0)  # 조회수 필드 추가
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # 이미지 필드 추가

    def __str__(self):
        return self.subject


class Comment(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class ProductCount(models.Model):
    ip = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.ip