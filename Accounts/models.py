from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    catagory = models.CharField(max_length=25, default="patient", null=True)
    
    def __str__(self) -> str:
        return super().__str__()