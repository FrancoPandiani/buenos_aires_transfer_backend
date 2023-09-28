from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import re
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


    




