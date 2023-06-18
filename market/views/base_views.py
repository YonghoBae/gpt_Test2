from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from ..models import Product, ProductCount, Category


def get_client_ip(request):  # Add this function
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request, category_name=''):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    category_list=Category.objects.all()
    if(category_name!=''):
        category = get_object_or_404(Category, name=category_name)
        product_list = Product.objects.filter(category=category)
    else:
        product_list = Product.objects.all()

    product_list = product_list.order_by('-create_date')

    if kw:
        product_list = product_list.filter(
            Q(name__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw)  # 내용 검색
        ).distinct()
    paginator = Paginator(product_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    if (category_name != ''):
        context = {'Product_list': page_obj, 'page': page, 'kw': kw, 'category_list': category_list, 'category': category}
    else:
        context = {'Product_list': page_obj, 'page': page, 'kw': kw, 'category_list': category_list}
    return render(request, 'market/Product_list.html', context)


def main(request):
    return render(request, 'market/mainpage.html')



def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    ip = get_client_ip(request)
    cnt = ProductCount.objects.filter(ip=ip, product=product).count()
    if cnt == 0:
        qc = ProductCount(ip=ip, product=product)
        qc.save()
        if product.view_count:
            product.view_count += 1
        else:
            product.view_count = 1
        product.save()
    context = {'product': product}
    return render(request, 'market/Product_detail.html', context)
