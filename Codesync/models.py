from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_superuser(self,email,phonenumber=None,password=None,**extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.phonenumber = phonenumber
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractUser): 
    username = models.CharField(unique=False)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    

    # class Meta: 
    REQUIRED_FIELDS = ['phonenumber']
    USERNAME_FIELD = 'email'
    # IMAGE_UPLOAD_PATH = 'profile_pics/'
    # profile_image = models.ImageField(upload_to=IMAGE_UPLOAD_PATH, blank=True, null=True)
    # bio = models.TextField(blank=True, null=True)

    objects = CustomUserManager()

