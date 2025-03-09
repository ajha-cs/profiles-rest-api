from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin 
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
#Base Classes to oveerride default django user model
#AbstractBaseUser: Base class for custom user model
#PermissionsMixin: To get deafult permission

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        #Normalising the email-address -> make it case insensitive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        #must be convertd to hashed pasword
        #set_password: To set password in hashed form -> provided by AbstractBaseUser
        user.set_password(password)
        #For saving django objects
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        #self gets automatically passed in
        user = self.create_user(email,name,password)
        
        user.is_superuser = True
        #Auto created by permissions mixin
        user.is_staff = True
        user.save(using=self._db)
        
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    #email: To store email of user
    name = models.CharField(max_length=255)
    #name: To store name of user
    is_active = models.BooleanField(default=True)
    #is_active: To check if user is active or not
    is_staff = models.BooleanField(default=False)
    #is_staff: To differentiate between normal user and admin user
    
    #Model manager for our object -> we need to use custom model 
    # manager to use our custom user model using django command line
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    #self: To refer to the object of the class
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self):
        #recommended for all django models -> to get meaningful output
        """Return string representation of our user"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profile Status Update"""
    #fk - used to connect one model with other model in django -> to maintain integrity
    user_profile = models.ForeignKey(
        #refernce to the user profile model rather than hardcoded it -> settings.AUTH_USER_MODEL
        settings.AUTH_USER_MODEL,
        #on_delete - what to do when the user profile is deleted
        # cascade the change down -> delete the feed item when the user is deleted
        # or NULL - set the user profile to NULL
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the model as a string"""
        return self.status_text