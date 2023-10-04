import json,uuid,re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from slugify import slugify


class UserAccountManager(BaseUserManager):

    def create_user(self,email,password=None,**extra_fields):
          
        # Regex que no permite usar el nombre de admin ni ningun caracter fuera de lo común.
        def create_slug(username):
            pattern_special_characters = r'\badmin\b|[!@#$%^~&*()_+-=[]{}|;:",.<>/?]|\s'
            if re.search(pattern_special_characters, username):
                raise ValueError('Username contains invalid characters')
            username = re.sub(pattern_special_characters, '', username)
            return slugify(username)
    
        if not email():
            raise ValueError('User must have a email address')
        
        # Lower case al email
        email = self.normalize_email(email)
        extra_fields['slug'] = create_slug(extra_fields['username'])
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,password,**extrafields):

        user=self.create_user(email, password,**extrafields)
        user.is_superuser = True
        user.is_staff = True
        user.role = "Admin"
        user.verified = True
        user.save(using=self.db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_online = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserAccountManager()

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='user_accounts_groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='user_accounts_permissions'
    )
    
    # Login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    roles = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('helper', 'Helper'),
        ('editor', 'Editor'),
        ('owner', 'Owner'),
    )

    role = models.CharField(max_length=20, choices=roles, default='customer')
    verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        counter = 1
        while UserAccount.objects.filter(slug=self.slug).exists():
            self.slug = f"{self.slug}-{counter}"
            counter += 1
        super().save(*args, **kwargs)

    def __str__(self):
        email_str = "".join(self.email)
        return email_str