from django.db import models

# Create your models here.


# to create a custom User models and admin panel (Start)
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_lazy


# Create your models here.

class MyCustomUserManager(BaseUserManager):
    """
    Custom user models manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, password, **extra_fields)


# Create User models
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, null=False)
    is_staff = models.BooleanField(ugettext_lazy('staff status'), default=False,
                                   help_text=ugettext_lazy('Designates whether the user can log in this site'))
    is_active = models.BooleanField(ugettext_lazy('active'), default=True,
                                    help_text='Designates whether this user should be treated as active. Unselect '
                                              'this instead of deleting accounts')
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    objects = MyCustomUserManager()

    def __str__(self):
        return self.email

    # optional
    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email
# to create a custom User models and admin panel (End)
