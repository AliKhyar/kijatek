from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,\
    BaseUserManager, PermissionsMixin
# Create your models here.




class UserManager(BaseUserManager):
    
    def create_user(self,email,password=None, **extra_fields):
        """create and saves a new user"""
        if not email:
            raise ValueError('User must have an email adress')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """create and saves a new super user """
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """custom user model to register with email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    departement_id = models.ForeignKey(Department, default=0, verbose_name="Departement", on_delete=models.SET_DEFAULT)
    city_origin_id = models.ForeignKey(City, default=0, verbose_name="City", on_delete=models.SET_DEFAULT)
    gender = models.CharField(max_length=1) #make:m female:m
    grad_date = models.DateField(verbose_name='Graduation date')
    semester = models.IntegerField('Semester', default=0)
    is_verified = models.BooleanField(default=False)
    verification_file = models.ImageField() ## add width and height
    file_type = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'

class establishmentStaff(User):
    role = models.CharField('Role', max_length=150)
    description = models.CharField('Description', max_length=250)

class establishment(models.Model):
    TYPE_CHOICES = [
    ('Private', "Private"),
    ('Public', "Public"),
    ('Semi', "Semi"),
    ]
    name = models.CharField('Name', max_length=250)
    director_id = models.ForeignKey(establishmentStaff, default=0, verbose_name='Director', on_delete=models.SET_DEFAULT)
    city_id = models.ForeignKey(City, default=0, verbose_name='City', on_delete=models.SET_DEFAULT)
    establishment_type = models.CharField('Private or Public', default='Public', choices=TYPE_CHOICES)
    fees = models.IntegerField('Fees', default=0)
    description = models.CharField('Description', max_length=250)
    adresse = adresse = models.CharField( max_length=250)
    phone = models.IntegerField()
    website = adresse = models.CharField('Website', max_length=250)

class Region(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    region_id = models.ForeignKey(Region, default=0, verbose_name='Region', on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Cities"

class Department(models.Model):
    responsible_id =  models.ForeignKey(establishmentStaff, default=0, verbose_name='Responsible', on_delete=models.SET_DEFAULT)
    establishment_id = models.ForeignKey(establishmentStaff, default=0, verbose_name='establishment', on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    grad = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    students_number = models.IntegerField()
    acceptance_criteria = models.CharField(max_length=200)

class Comment(models.Model):
    department_id = models.ForeignKey(Department, default=1, verbose_name="Department", on_delete=models.SET_DEFAULT)
    user = models.ForeignKey(User,default=0, on_delete=models.SET_DEFAULT)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)
    
    def was_commented_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.body

class Reply(models.Model):
    comment_id = models.ForeignKey(Comment,default=0, on_delete=models.SET_DEFAULT)
    user_id = models.ForeignKey(User,default=0, verbose_name="Forum", on_delete=models.SET_DEFAULT)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

class Question(models.Model):
    user_id = models.ForeignKey(User,default=0, on_delete=models.SET_DEFAULT)
    body = models.TextField(max_length=250)
    about = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort in chronological order by default
        ordering = ('created',)
    
    def was_commented_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.body

class Answer(models.Model):
    user_id = models.ForeignKey(User,default=0, on_delete=models.SET_DEFAULT)
    comment_id = models.ForeignKey(Comment,default=0, on_delete=models.SET_DEFAULT)
    body = models.TextField(max_length=250)
    about = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort in chronological order by default
        ordering = ('created',)
    
    def was_commented_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.body

class Review(models.Model):
    user_id = models.ForeignKey(User,default=0, on_delete=models.SET_DEFAULT)
    department_id = models.ForeignKey(Department,default=0, on_delete=models.SET_DEFAULT)
    review = models.IntegerField()
    feedback = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # sort in chronological order by default
        ordering = ('created',)
    
    def was_commented_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.body
     