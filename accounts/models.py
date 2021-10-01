from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
 
    def create_user(self, email,username, password=None):
       
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The username must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,username, password):

    	user = self.create_user(
    		email=self.normalize_email(email),
    		username=username,
    		password =password,)
    	user.is_admin =True
    	user.is_staff =True
    	user.is_superuser =True
    	user.save()
    	return user              
        

class CustomBaseUser(AbstractBaseUser):
	email = models.EmailField(verbose_name='email',max_length=60,unique=True)
	username = models.CharField(max_length=25,unique=True)
	address = models.CharField(max_length=100,blank=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.username

	def has_perm(self,perm,obj=None):
		return self.is_admin

	def has_module_perms(self,app_label):
		return True

