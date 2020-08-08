from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'student'

urlpatterns = [
    path('',views.StudentBaseView.as_view(),name='index'),
    path('signup/',views.StudentSignUpView.as_view(),name='student_signup'),
    #path('login/', views.TeacherLoginView.as_view(), name='student_login'),
    #path('logout/',auth_views.LogoutView.as_view(template_name='registration/student_logout.html'),name="student_logout")
]
