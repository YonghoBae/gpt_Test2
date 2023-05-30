from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Product, Comment


@login_required(login_url='common:login')
def Comment_create(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.buyer = request.user  # buyer 속성에 로그인 계정 저장
            comment.create_date = timezone.now()
            comment.product = product
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('market:detail', product_id=product.id), comment.id))
    else:
        form = CommentForm()
    context = {'product': product, 'form': form}
    return render(request, 'market/Product_detail.html', context)


@login_required(login_url='common:login')
def Comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.buyer:
        messages.error(request, '수정권한이 없습니다')
        return redirect('market:detail', product_id=comment.product.id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(resolve_url('market:detail', product_id=comment.product.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'market/Comment_form.html', context)


@login_required(login_url='common:login')
def Comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.buyer:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('{}#comment_{}'.format(resolve_url('market:detail', product_id=comment.product.id), comment.id))


@login_required(login_url='common:login')
def Comment_vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user in comment.voter.all():
        comment.voter.remove(request.user)
    else:
        comment.voter.add(request.user)
    return redirect('market:detail', product_id=comment.product.id)
