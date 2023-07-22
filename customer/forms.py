from django.contrib.auth.models import User
from django import forms
import re
from .models import Contact,Customer

username_compiler=re.compile(r'^\w{5,}$')


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput( attrs={'class':'form-control','placeholder':'first name'}))
    last_name=forms.CharField(widget=forms.TextInput( attrs={'class':'form-control','placeholder':'last name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    username=forms.CharField(widget=forms.TextInput( attrs={'class':'form-control','placeholder':'username'}))
    password=forms.CharField(widget=forms.PasswordInput( attrs={'class':'form-control','placeholder':'password'}))
    password_again=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password_again'}))


    def save(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        # user.first_name = first_name
        # user.last_name = last_name
        # user.save()

        customer = Customer.objects.create(user=user)
        return customer
    
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if not username_compiler.match(username):
    #         raise forms.ValidationError('Istifadeci adi yanlisdir')
    #     elif User.objects.filter(username=username).exists():
    #         raise forms.ValidationError('Istifadeci adi artiq bir defe istifade olunub')
        
    #     return username
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError('bu email adi artiq bir defe istifade olunub')
        
    #     return email
    
    # def clean_password(self):
        
    #     password = self.cleaned_data['password']
    #     password_again = self.cleaned_data.get('password_again')
    #     if password and password_again and password!=password_again:
    #         raise forms.ValidationError('daxil etdiyiniz sifre yanlisdir')
        
        # return password


    

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'username'}))


    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )
        clear = Customer.objects.create(user=user)
        return clear



class ContactForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Contact
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Email'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
            'message':forms.Textarea(attrs={'class':'form-control','placeholder':'message','rows':'8'}),
        }

