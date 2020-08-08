from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User
from .forms import TeacherSignUpForm, TeacherAuthenticationForm, StudentSignUpForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorators import teacher_required
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.urls import reverse
# Create your views here

def index(request):
    return redirect('teacher:index')

class TeacherLoginView(TemplateView):
    template_name = 'registration/teacher_login.html'

@method_decorator([login_required(login_url='teacher:teacher_login'),teacher_required(login_url='teacher:teacher_login')], name='dispatch')
class TeacherBaseView(TemplateView):
    template_name = 'mcq_app/teacher_base.html'
    
#@method_decorator([login_required(login_url='student:student_login')], name='dispatch')
class StudentBaseView(TemplateView):
    template_name = 'mcq_app/student_base.html'

def teacher_signup(request):
    return render(request,'mcq_app/teacher_signup.html')

class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'mcq_app/teacher_signup.html'

    def get_context_data(self, **kwargs):
        print('######################################################')
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print('---------------------------------------------------------')
        user = form.save()
        login(self.request, user)
        return redirect('teacher:index')
    
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/student_signup.html'

    def get_context_data(self, **kwargs):
        print('######################################################')
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print('---------------------------------------------------------')
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('student:index')
    
class TeacherLoginView(auth_views.LoginView):
    template_name = "registration/teacher_login.html"
    authentication_form = TeacherAuthenticationForm
    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        # elif self.request.user.is_superuser:
        #     return reverse("admin")
        else:
            return reverse("teacher:index")
    
    
    
    
    
    
    
    
    
    
    
    
    