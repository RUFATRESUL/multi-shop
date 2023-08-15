from django import forms
from .models import Orded,OrderProduct

class OrderForm(forms.ModelForm):
    class Meta:
        exclude = ['customer','coupon_code','coupon_discount','accepted','delivered','created']
        model = Orded
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'John'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Doe'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'example@gmail.com'}),
            'mobile': forms.TextInput(attrs={'class':'form-control','placeholder':'123456789'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder':'Baku'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Random Adress'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'AZE12345'}),
            'country': forms.Select(attrs={'class':'custom-select'}),
            'phone_code':forms.Select(attrs={'class':'custom-select'})
        }


    def save(self,customer,basketlist,coupon):
        data = self.cleaned_data.copy()
        data['customer'] = customer
        print(coupon.code)
        if coupon and coupon.is_valid(customer)[0]:
            data['coupon_code'] = coupon.code
            data['coupon_discount'] = coupon.discount
        order = Orded.objects.create(**data)


        order_products =[]
        for basketitem in basketlist:
            op = OrderProduct(
                order=order,
                title=basketitem.product.title,
                count=basketitem.count,
                price=basketitem.product.price,
                size=basketitem.size.title,
                color=basketitem.color.title

            )
            order_products.append(op)
        OrderProduct.objects.bulk_create(order_products)
        
        


