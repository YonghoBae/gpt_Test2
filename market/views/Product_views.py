from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import ProductForm
from ..models import Product


@login_required(login_url='common:login')
def Product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product = form.save(commit=False)
            Product.seller = request.user  # author 속성에 로그인 계정 저장
            Product.create_date = timezone.now()
            Product.price = form.cleaned_data['price']
            Product.save()
            return redirect('market:index')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'market/Product_form.html', context)


@login_required(login_url='common:login')
def Product_modify(request, Product_id):
    Product = get_object_or_404(Product, pk=Product_id)
    if request.user != Product.seller:
        messages.error(request, '수정권한이 없습니다')
        return redirect('market:detail', Product_id=Product.id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=Product)
        if form.is_valid():
            Product = form.save(commit=False)
            Product.modify_date = timezone.now()  # 수정일시 저장
            Product.save()
            return redirect('market:detail', Product_id=Product.id)
    else:
        form = ProductForm(instance=Product)
    context = {'form': form}
    return render(request, 'market/Product_form.html', context)


@login_required(login_url='common:login')
def Product_delete(request, Product_id):
    question = get_object_or_404(Product, pk=Product_id)
    if request.user != question.seller:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('market:detail', question_id=question.id)
    question.delete()
    return redirect('market:index')


@login_required(login_url='common:login')
def Product_vote(request, Product_id):
    Product = get_object_or_404(Product, pk=Product_id)
    if request.user == Product.seller:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        Product.voter.add(request.user)
    return redirect('market:detail', Producgt_id=Product.id)