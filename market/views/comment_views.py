from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Product, Comment


@login_required(login_url='common:login')
def Comment_create(request, Product_id):
    Product = get_object_or_404(Product, pk=Product_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.buyer = request.user  # buyer 속성에 로그인 계정 저장
            Comment.create_date = timezone.now()
            Comment.Product = Product
            Comment.save()
            return redirect('{}#Comment_{}'.format(resolve_url('market:detail', Product_id=Product.id), Comment.id))
    else:
        form = CommentForm()
    context = {'Product': Product, 'form': form}
    return render(request, 'market/Product_detail.html', context)


@login_required(login_url='common:login')
def Comment_modify(request, Comment_id):
    Comment = get_object_or_404(Comment, pk=Comment_id)
    if request.user != Comment.buyer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('market:detail', Product_id=Comment.Product.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=Comment)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.modify_date = timezone.now()
            Comment.save()
            return redirect('{}#Comment_{}'.format(resolve_url('market:detail', Product_id=Comment.Product.id), Comment.id))
    else:
        form = CommentForm(instance=Comment)
    context = {'Comment': Comment, 'form': form}
    return render(request, 'market/Comment_form.html', context)


@login_required(login_url='common:login')
def Comment_delete(request, Comment_id):
    Comment = get_object_or_404(Comment, pk=Comment_id)
    if request.user != Comment.buyer:
        messages.error(request, '삭제권한이 없습니다')
    else:
        Comment.delete()
    return redirect('{}#Comment_{}'.format(resolve_url('market:detail', Product_id=Comment.Product.id), Comment.id))


@login_required(login_url='common:login')
def Comment_vote(request, Comment_id):
    Comment = get_object_or_404(Comment, pk=Comment_id)
    if request.user in Comment.voter.all():
        Comment.voter.remove(request.user)
    else:
        Comment.voter.add(request.user)
    return redirect('market:detail', Product_id=Comment.Product.id)
