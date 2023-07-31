from django.contrib.auth.models import User
from django import forms

from .models import Contact,Customer
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox



class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class':'form-control','placeholder':'first name'}))
    last_name=forms.CharField(max_length=50, widget=forms.TextInput( attrs={'class':'form-control','placeholder':'last name'}))
    email=forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    username=forms.CharField(max_length=100, widget=forms.TextInput( attrs={'class':'form-control','placeholder':'username'}))
    password=forms.CharField(max_length=50, widget=forms.PasswordInput( attrs={'class':'form-control','placeholder':'password'}))
    password_again=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password_again'}))
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
        
    def clean(self):

        cleaned_data=super().clean()
        password = cleaned_data.get('password')
        password_again = cleaned_data.get('password_again')

        if password and password_again and password!=password_again:
            raise forms.ValidationError('daxil etdiyiniz sifre yanlisdir !')
       
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('bu email adi artiq bir defe istifade olunub !')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
      
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Istifadeci adi yanlisdir !')
        return username


    def save(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        new_user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        customer = Customer.objects.create(user=new_user)
        return customer
    

    




    

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'username'}))


#     def save(self):
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']

#         user = User.objects.create_user(
#             username=username,
#             password=password
#         )
#         clear = Customer.objects.create(user=user)
#         return clear


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    # Add max_length attribute for the 'subject' field if needed

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': '8'}))

