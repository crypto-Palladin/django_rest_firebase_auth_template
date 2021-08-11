from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# _____________________________________________________________________________________________________________________
# Custom USER Model to use email as unique field
# ___________________________
class CustomUserManager(BaseUserManager):
    # first_name, last_name,
    def create_user(self, email, username=None, password=None):
        if not email:
            raise ValueError("User must have an email")
        # if not first_name:
        #    raise ValueError("User must have a first name")
        # if not last_name:
        #    raise ValueError("User must have a last name")

        user = self.model(
            email=self.normalize_email(email)
        )
        # user.first_name = first_name
        # user.last_name = last_name
        user.set_password(password)
        print(user.password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        # if not first_name:
        #    raise ValueError("User must have a first name")
        # if not last_name:
        #     raise ValueError("User must have a last name")

        user = self.model(
            email=self.normalize_email(email)
        )
        # user.first_name = first_name
        # user.last_name = last_name
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    # Email should be used instead of username
    email = models.EmailField('email address', unique=True)
    # user's name and surname
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    # Boolean fields to distinct users role
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return "{0} {1} - email: {2}".format(self.first_name, self.last_name, self.email)


