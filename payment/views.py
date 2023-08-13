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
    coupun_code = request.GET.get('coupon')
    # coupun_message = None
    coupun_status = None
    coupun_discount = 0
    coupun_discount_amount = 0
    coupon = None

    if coupun_code:
        coupun = Coupon.objects.filter(code=coupun_code).first()
        if coupun:
            is_valid,message = coupun.is_valid(request.user.customer)
            if is_valid:
                coupun_status='valid'
                coupun_discount = coupun.discount
                coupun_discount_amount = final_price * coupun_discount / 100
                # all_price -= coupun_discount_amount
                final_price -= coupun_discount_amount
            else:
                coupun_status ='invalid'
                
        else:
            coupun_status ='invalid'

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
        'coupon_status':coupun_status,
        'coupun_discount':coupun_discount,
        'coupun_discount_amount':round(coupun_discount_amount,2),
        'coupun_code':coupun_code

    })


