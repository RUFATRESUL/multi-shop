from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Category,Company,Prouduct,Color,Size
from django.db.models import Count,Avg
from customer.models import Review,Reply
from django.core.paginator import Paginator
from .filters import ProductFilter
from django.urls import reverse

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


def product_detail(request,pk,slug):
    product=get_object_or_404(Prouduct,pk=pk)
    total_review = Review.objects.filter(product=product).count()
   
    current_review = None
    if(request.user.is_authenticated and request.user.customer):
        current_review = Review.objects.filter(customer=request.user.customer,product=product).first()
    
    similar_products = product.get_similar_products()
    return render(request,'product-detail.html',{
        'product':product,
        'current_review':current_review,
        'total_review':total_review,
        'similar_products':similar_products
        
    })

def shop(request):
    products = Prouduct.objects.all().annotate(avg_star=Avg('reviews__star_count'), review_count=Count('reviews')) 
     
    search_input = request.GET.get('search')
    if search_input:
        products = products.filter(title__icontains=search_input)

    product_filter = ProductFilter(request.GET,products)
    products = product_filter.qs
    colors = Color.objects.all().annotate(product_count=Count('product'))
    sizes = Size.objects.all().annotate(product_count=Count('prouduct'))

    sorting_input = request.GET.get('sorting')
    if sorting_input:
        if sorting_input == '-avg_star':
            products = products.order_by('avg_star','-review_count')
        else:
            products = products.order_by(sorting_input)


    page_by_input = int(request.GET.get('page_by',4))
    page_number = int(request.GET.get('page',1))
    paginator = Paginator(products,page_by_input)
    page = paginator.page(page_number)
    products = page.object_list

   
    return render(request,'shop.html',{
        'products':products,
        'paginator':paginator,
        'page': page,
        'colors':colors,
        'sizes':sizes,
        })



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
        
        return redirect('shop:product-detail', pk=product.pk, slug=product.slug)
    return redirect('shop:product-detail', pk=product.pk, slug=product.slug)
    


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

        return redirect(reverse('shop:product-detail', kwargs={'pk': pk, 'slug': review.product.slug}))

    return HttpResponse(status=400)  



