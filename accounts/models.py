from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
# Create your models here.
    class Meta:
        verbose_name_plural = 'CustomUser'
