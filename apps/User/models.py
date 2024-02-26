from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):
    # Создание пользователя
    def create(self, email, password=None, **extra_fields):
        # print(email, password, extra_fields)
        email = self.normalize_email(email)
        if not email:
            raise ValueError('Поле электронной почты должно быть задано!')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Создание суперпользователя
    def create_superuser(self, email,  password, **extra_fields):
        user = self.create(email, password=password)
        user.is_superuser = True   
        user.is_staff = True
        user.save(using=self._db)
        return user  


# Модель пользователя
class User(AbstractUser):
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email', 'phone']
    
    
    objects = UserManager()
    def __str__(self):
        return self.username
    