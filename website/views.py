from django.shortcuts import render , redirect
from website.models import *
from website.forms import *

def form1(request) :
 if request.method == "POST" :
    form1 = ContactForm(request.POST)
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")
    subject = request.POST.get("subject")
    if form1.is_valid() :
     print(name , email , subject ,  message)
     return redirect(success)
    else :
     form1 = ContactForm() 
 form = ContactForm()

 return render(request,"form1.html" , {"form":form})

def form2(request) :
  if request.method == "POST" :
        form = FeedBackForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        if form.is_valid() :
            print(name , email , message)
            print(request.POST)
            obj = FeedBack()
            obj.name = name
            obj.email = email
            obj.message = message
            obj.save()
            return redirect("website:success")

        else :
         form = FeedBackForm()      
  form2 = FeedBackForm()

 
  return render(request,"form2.html" , {"form2":form2})


def success(request):
    return render(request, "success.html")

# def form3(request):
#     return render(request, "form3.html")