from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from stock.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True
    )
    kakao_nickname = models.CharField(
        verbose_name='Kakao Nickname',
        max_length=32
    )
    kakao_email = models.CharField(
        verbose_name='Kakao Email',
        null=True,
        blank=True,
        max_length=64
    )
    stock_code_1 = models.CharField(
        verbose_name='stock_code_1',
        null=True,
        blank=True,
        max_length=8
    )
    stock_code_2 = models.CharField(
        verbose_name='stock_code_2',
        null=True,
        blank=True,
        max_length=8
    )
    stock_code_3 = models.CharField(
        verbose_name='stock_code_3',
        null=True,
        blank=True,
        max_length=8
    )
    is_active = models.BooleanField(
        verbose_name='is active',
        default=True
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
