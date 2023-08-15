from django.shortcuts import render,redirect
from .models import Coupon
from django.db.models import Sum,F
from .forms import OrderForm
# Create your views here.

def checkout(request):
    basketlist = request.user.customer.basketlist.all().annotate(total_price=F('count')*F('product__price'))
    all_price = basketlist.aggregate(all_price=Sum('total_price'))['all_price'] or 0
    shipping_price = all_price * 0.07
    final_price = all_price + shipping_price
    coupon_code = request.GET.get('coupon')
    # coupon_message = None
    coupon_status = None
    coupon_discount = 0
    coupon_discount_amount = 0
    coupon = None

    if coupon_code:
        coupon = Coupon.objects.filter(code=coupon_code).first()
        if coupon:
            is_valid,message = coupon.is_valid(request.user.customer)
            if is_valid:
                coupon_status='valid'
                coupon_discount = coupon.discount
                coupon_discount_amount = final_price * coupon_discount / 100
                # all_price -= coupon_discount_amount
                final_price -= coupon_discount_amount
            else:
                coupon_status ='invalid'
                
        else:
            coupon_status ='invalid'

    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(request.user.customer,basketlist,coupon)
            return redirect('shop:index')


    return render(request,'checkout.html',{
        'form':form,
        'basketlist':basketlist,
        'all_price':round(all_price,2),
        'shipping_price':round(shipping_price,2),
        'final_price':round(final_price,2),
        'coupon_status':coupon_status,
        'coupon_discount':coupon_discount,
        'coupon_discount_amount':round(coupon_discount_amount,2),
        'coupon_code':coupon_code

    })


