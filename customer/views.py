from django.shortcuts import render,redirect,get_object_or_404
from .models import WishItem,BasketItem
from .forms import RegisterForm,ContactForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from shop.models import Prouduct
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,F
from payment.models import Coupon


# Create your views here.
@login_required
def basket(request):
    basketlist = request.user.customer.basketlist.all().annotate(total_price=F('count')*F('product__price'))
    all_price = basketlist.aggregate(all_price=Sum('total_price'))['all_price'] or 0
    shipping_price = all_price * 0.07
    final_price = all_price + shipping_price

    coupon_code = request.GET.get('coupon')
    coupon_message = None
    coupon_status = None
    coupon_discount = 0
    coupon_discount_amount = 0

    if coupon_code:
        coupon = Coupon.objects.filter(code=coupon_code).first()
        if coupon:
            is_valid, message = coupon.is_valid(request.user.customer)
            if is_valid:
                coupon_status='valid'
                coupon_message = message
                coupon_discount = coupon.discount
                coupon_discount_amount = final_price * coupon_discount / 100
                final_price -= coupon_discount_amount
            else:
                coupon_status ='invalid'
                coupon_message = message 
        else:
            coupon_status ='invalid'
            coupon_message = 'Bele bir kupon yoxdur'


   

    return render(request,'basket.html',
    {'basketlist':basketlist,
    'all_price':round(all_price,2),
    'shipping_price':round(shipping_price,2),
    'final_price':round(final_price,2),
    'coupon_status':coupon_status,
    'coupon_message':coupon_message,
    'coupon_discount':coupon_discount,
    'coupon_discount_amount':round(coupon_discount_amount,2),
    'coupon_code':coupon_code
    })


def add_basket(request,product_pk):
    if request.method=="POST":
        size_pk = request.POST.get('size')
        color_pk = request.POST.get('color')
        count_pk = request.POST.get('count')
        customer = request.user.customer
        basket = BasketItem.objects.create(product_id=product_pk,
                                           size_id=size_pk,
                                           color_id=color_pk,
                                           count=count_pk,
                                           customer=customer)
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('shop:index')
    

def increase_basket_item(request,basket_pk):
    basket = get_object_or_404(BasketItem,pk=basket_pk)
    basket.count = F('count')+1
    basket.save()
    return redirect('customer:basket')


def decrease_basket_item(request,basket_pk):
    basket = get_object_or_404(BasketItem,pk=basket_pk)
    if basket.count == 1:
        basket.delete()
    else:
        basket.count = F('count')-1
        basket.save()
    return redirect('customer:basket')

@login_required
def remove_basket(request,basket_pk):
    basket = get_object_or_404(BasketItem,pk=basket_pk)
    basket.delete()
    return redirect('customer:basket')


def wishlist_view(request):
    wishlist = request.user.customer.wishlist.all()
    total_price = wishlist.aggregate(total_price=Sum('product__price'))['total_price']
    return render(request,'wishlist.html',{'wishlist':wishlist,'total_price':total_price})

@login_required
def wish_product(request,pk):
    product = get_object_or_404(Prouduct,pk=pk)
    customer =request.user.customer
    wishitem = WishItem.objects.create(product=product,customer=customer)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def unwish_product(request,pk):
    product = get_object_or_404(Prouduct,pk=pk)
    customer =request.user.customer
    wishitem = WishItem.objects.filter(product=product,customer=customer).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def contact(request):
    form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'contact.html',{'form':ContactForm,'result':'success'})
        return render(request,'contact.html',{'form':form,'result':'fail'})
    return render(request,'contact.html',{'form':form})


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request,customer.user)
            return redirect('customer:login')
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            nextUrl = request.GET.get('next')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('shop:index')
        return render(request, 'login.html', context={'unsuccess': True, })

    
def logout_view(request):
    logout(request)
    return redirect('customer:login')


usd_eq = {'AZN':1.7,'TRY':27.1,'EUR':0.92,'USD':1}

def change_currency(request):
    currency = request.GET.get('currency')
    currency_ratio = usd_eq[currency]
    request.session['currency'] = currency
    request.session['currency_ratio'] = currency_ratio
    
    return redirect(request.META.get('HTTP_REFERER'))
