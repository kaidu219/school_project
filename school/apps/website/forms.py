from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Student, Class, Teacher


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class TeacherRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=20)
    subject = forms.CharField(max_length=100)
    class_group_student = forms.ModelChoiceField(queryset=Class.objects.all())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = ['username', 'full_name', 'phone_number', 'subject',
                  'class_group_student', 'password1', 'password2']


class PhoneNumberLoginForm(forms.Form):
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
