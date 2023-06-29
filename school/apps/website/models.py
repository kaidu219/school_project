from django.db import models
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    """
    Модель 'Школа'
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='Class')

    def __str__(self):
        return self.name


class Teacher(AbstractUser):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    class_group_student = models.ForeignKey(
        Class, on_delete=models.SET_NULL, null=True, related_name='teacher')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='teachers',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='teachers',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'Teacher'

    # USERNAME_FIELD = 'phone_number'
    # REQUIRED_FIELDS = []


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    birth_date = models.DateField()
    class_name = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='student')
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __str__(self):
        return self.full_name
