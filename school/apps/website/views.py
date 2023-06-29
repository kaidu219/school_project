from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth, messages
from django.db.models import Q

from config.settings import EMAIL_HOST_USER

from .models import Student
from .forms import (StudentForm, EmailForm,
                    TeacherRegistrationForm,
                    PhoneNumberLoginForm, SearchForm,)


class TeacherRegistrationView(View):
    def get(self, request):
        form = TeacherRegistrationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('student_list')
        return render(request, 'registration.html', {'form': form})


class TeacherLoginView(View):
    def get(self, request):
        form = PhoneNumberLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = PhoneNumberLoginForm(request.POST)

        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = auth.authenticate(
            request, phone_number=phone_number, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('student_list')
        else:
            return render(request, 'login.html', {'form': form})


class StudentListView(LoginRequiredMixin, View):
    def get(self, request):
        students = Student.objects.filter(
            class_name=request.user.class_group_student)
        return render(request, 'student_list.html', {'students': students})


class StudentDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)
        return render(request, 'student_detail.html', {'student': student, 'form': form})

    # def post(self, request, pk):
        # student = get_object_or_404(Student, pk=pk)
        # form = StudentForm(request.POST, instance=student)
        # if form.is_valid():
        #     form.save()
        #     return redirect('student_list')
        # return render(request, 'student_detail.html', {'student': student, 'form': form})


class EditStudentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)
        return render(request, 'edit_student.html', {'student': student, 'form': form})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=pk)
        return render(request, 'edit_student.html', {'student': student, 'form': form})


class StudentDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('student_list')


class StudentCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'create_student.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Student.objects.filter(email=email).exists():
                form.add_error(
                    'email', 'Ученик с таким адресом электронной почты уже существует.')
            else:
                student = form.save()

                school = student.class_name.school
                class_name = student.class_name.name
                teacher = student.class_name.teacher

                subject = f'Добро пожаловать в школу {school}'
                message = f'Дорогой {student.full_name},\n\nДобро пожаловать в нашу школу {school}!'
                message += f'Вы были добавлены в класс {class_name} под руководством учителя {teacher}.'
                from_email = EMAIL_HOST_USER
                to_email = student.email
                send_mail(subject, message, from_email, [to_email])

                return redirect('student_list')
        return render(request, 'create_student.html', {'form': form})


class SearchStudentsView(LoginRequiredMixin, View):
    def get(self, request):
        form = SearchForm()
        return render(request, 'search_students.html', {'form': form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            results = Student.objects.filter(
                Q(full_name__icontains=search_query) | Q(email__icontains=search_query))
            return render(request, 'search_results.html', {'form': form, 'results': results})
        return render(request, 'search_results.html', {'form': form})


class SendEmailView(LoginRequiredMixin, View):
    def get(self, request):
        form = EmailForm()
        return render(request, 'send_email.html', {'form': form})

    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            students = Student.objects.filter(
                class_name=request.user.class_group_student)
            emails = [student.email for student in students]
            send_mail(subject, message, EMAIL_HOST_USER, emails)
            return redirect('student_list')
        return render(request, 'send_email.html', {'form': form})
