from django.urls import path
from apps.website.views import (
    TeacherRegistrationView, TeacherLoginView, StudentListView,
    StudentDetailView, StudentDeleteView, StudentCreateView,
    SearchStudentsView, SendEmailView, EditStudentView
)

urlpatterns = [
    path('register/', TeacherRegistrationView.as_view(), name='register'),
    path('login/', TeacherLoginView.as_view(), name='login'),

    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/',
         StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/',
         EditStudentView.as_view(), name='edit_student'),
    path('students/<int:pk>/delete/',
         StudentDeleteView.as_view(), name='student_delete'),
    path('students/create/', StudentCreateView.as_view(), name='create_student'),

    path('search/', SearchStudentsView.as_view(), name='search_students'),

    path('send-email/', SendEmailView.as_view(), name='send_email'),
]
