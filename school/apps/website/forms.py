from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Student, Class, Teacher


class StudentForm(forms.ModelForm):
    photo = forms.ImageField(required=False, label='Фотография')

    class Meta:
        model = Student
        fields = ['full_name', 'email', 'birth_date',
                  'class_name', 'address', 'gender', 'photo']


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Тема')
    message = forms.CharField(widget=forms.Textarea, label='Текст письма')


class TeacherRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150, label='ФИО')
    phone_number = forms.CharField(max_length=20, label='Номер телефона')
    subject = forms.CharField(max_length=100, label='Предмет')
    class_group_student = forms.ModelChoiceField(
        queryset=Class.objects.all(), label='Класс')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Повторите пароль', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = ['username', 'full_name', 'phone_number', 'subject',
                  'class_group_student', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.subject = self.cleaned_data['subject']
        user.class_group_student = self.cleaned_data['class_group_student']

        password = self.cleaned_data['password1']
        user.set_password(password)

        if commit:
            user.save()
        return user


class PhoneNumberLoginForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', max_length=20)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск', max_length=100)
