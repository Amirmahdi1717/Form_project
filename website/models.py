from django.db import models
from django.utils import timezone

class FeedBack(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField() 
    message = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta :
        ordering = ['-created']

    def __str__(self):
        return f"{self.name}"
    

# class Login(models.Model) :
#     name = models.CharField(max_length=100),
#     password = models.CharField(max_length=100)    
