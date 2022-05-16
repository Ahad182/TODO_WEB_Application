from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TODOMODEL(models.Model):
    STATUS_CHOICES= [
        ('C','Completed'),
        ('p','Pending'),
    ]

    PRIORIYY_CHOICES= [
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
    ]


    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=30, choices=PRIORIYY_CHOICES)

    def __str__(self):
        return self.title 