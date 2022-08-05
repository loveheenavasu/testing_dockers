from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, )
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)
    permissions = ArrayField(models.CharField(max_length=10, blank=True, null=True), size=8,)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


class UserManager(BaseUserManager):
    def _create_user(self, email: str, password: str = None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str = None, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self._create_user(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        'email address',
        max_length=255,
        unique=True,
        error_messages={'unique': "A user with that email already exists.", }
    )
    is_email_verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_general_manager = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField('active',
                                    default=True,
                                    help_text=('Designates whether this user should be treated as active. '
                                               'Unselect this instead of deleting accounts.'
                                               ),
                                    )
    is_staff = models.BooleanField('staff status',
                                   default=False,
                                   help_text='Designates whether the user can log into this admin site.',
                                   )
    date_joined = models.DateTimeField(auto_now_add=True)
    contact = models.BigIntegerField(null=True, blank=True)
    is_contact_verified = models.BooleanField(default=False)
    company_name = models.CharField(max_length=300, null=True, blank=True)
    logo = models.CharField(max_length=300, null=True, blank=True)
    tab_number = models.IntegerField(null=True, blank=True, default=4)
    image = models.CharField(max_length=300, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
