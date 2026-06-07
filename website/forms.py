from django import forms
from website.models import *

class ContactForm(forms.Form) :
    name = forms.CharField(max_length=100,label="نام")
    email = forms.EmailField(label="ایمیل")
    subject = forms.CharField(max_length=200,label="موضوع")
    message = forms.CharField(widget=forms.Textarea,label="متن")




class FeedBackForm(forms.ModelForm) :
    class Meta:
     model = FeedBack
     fields = ["name" , "email" , "message"]