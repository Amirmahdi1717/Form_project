from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('contact/', form1 , name='form1'),              
    path('feedback/', form2 , name='form2'),              
    path('success/', success , name='success'),            
    # path('form3/', form3 , name='form3'),            

]
