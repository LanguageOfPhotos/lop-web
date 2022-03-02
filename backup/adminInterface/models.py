from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    which_user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='images/',
                              default='images/default.jpg')

    is_verified = models.BooleanField(default=False)


    class Meta:
        ordering = ['-updated_at']