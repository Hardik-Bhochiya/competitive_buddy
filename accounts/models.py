from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles/", default="profiles/default.png")
    college = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    cf_handle = models.CharField(max_length=100, blank=True)
    lc_handle = models.CharField(max_length=100, blank=True)
    cc_handle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username