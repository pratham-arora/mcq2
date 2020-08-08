from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'teacher'

urlpatterns = [
    path('',views.TeacherBaseView.as_view(),name='index'),
    path('signup/',views.TeacherSignUpView.as_view(),name='teacher_signup'),
    path('login/', views.TeacherLoginView.as_view(), name='teacher_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/teacher_logout.html'),name="teacher_logout")
]
