from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Category,Company,Prouduct,ProuductImages
from django.db.models import Count
from customer.models import Review,Reply

# Create your views here.

def index(request):
    slide_company = Company.objects.filter(is_slide=True)[:3]
    nonslide_company = Company.objects.filter(is_slide=False)[:4]
    categories = Category.objects.annotate(prouduct_count=Count('prouduct'))
    new_product = Prouduct.objects.all().order_by('-created')[:8]
    featured_products = Prouduct.objects.filter(featured=True)
    return render(request,'index.html',{
       'slide_company':slide_company,
       'nonslide_company':nonslide_company,
       'categories':categories,
       'new_product':new_product,
       'featured_products':featured_products,
       
       
    })

def product_detail(request,pk):
    product=get_object_or_404(Prouduct,pk=pk)
    current_review = None
    if(request.user.is_authenticated and request.user.customer):
        current_review = Review.objects.filter(customer=request.user.customer,product=product).first()

    return render(request,'product-detail.html',{
        'product':product,
        'current_review':current_review
    })

def shop(request):
    return render(request,'shop.html')

def review(request,pk):
    if request.method == 'POST':
        customer = request.user.customer 
        product = get_object_or_404(Prouduct,pk=pk)
        if Review.objects.filter(customer=customer,product=product).exists():
            return HttpResponse(status=403)
        star_count = int(request.POST.get('star_count'))
        comment = request.POST.get('comment')
        Review.objects.create(
            customer=customer,product=product,
            star_count=star_count,comment=comment,

        )
        return redirect('shop:product-detail',pk=pk)
    return redirect('shop:product-detail',pk=pk)

def reply_review(request, pk):
    if request.method == 'POST':
        review = get_object_or_404(Review, pk=pk)
        reply_comment = request.POST.get('reply_comment')

        if reply_comment:
            Reply.objects.create(
                review=review,
                user=request.user,
                comment=reply_comment
            )

        return redirect('shop:product-detail', pk=review.product.pk)

    return HttpResponse(status=400)  

