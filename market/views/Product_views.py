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
            product = form.save(commit=False)
            product.seller = request.user  # author 속성에 로그인 계정 저장
            product.create_date = timezone.now()
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('market:index')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'market/Product_form.html', context)


@login_required(login_url='common:login')
def Product_modify(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.seller:
        messages.error(request, '수정권한이 없습니다')
        return redirect('market:detail', product_id=product.id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.modify_date = timezone.now()  # 수정일시 저장
            product.save()
            return redirect('market:detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'market/Product_form.html', context)


@login_required(login_url='common:login')
def Product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.seller:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('market:detail', product_id=product.id)
    product.delete()
    return redirect('market:index')


@login_required(login_url='common:login')
def Product_vote(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user == product.seller:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        product.voter.add(request.user)
    return redirect('market:detail', product_id=product.id)