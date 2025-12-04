from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, username=username, password=password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repo_name = models.CharField(max_length=255)
    repo_content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    repo_description = models.TextField(blank=True, null=True)          # NEW: description
    repo_visiblity = models.CharField(                                    # NEW: visibility (note spelling used in views/templates)
        max_length=10,
        choices=(('public', 'public'), ('private', 'private')),
        default='private'
    )
    language_mode = models.CharField(max_length=50, blank=True, null=True) # NEW: editor mode (optional)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.repo_name}"


# class settings(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_settings")


