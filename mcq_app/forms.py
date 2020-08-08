from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Teacher, Student, User
from django import forms


class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email','required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email','required': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Email','required': True,'autofocus' : True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Password','required': True}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Password','required': True}))
    
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control', 'name':'avatar-file', 'type':'file'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name", "profile_pic")
        # widgets = {
        #  'photo': FileInput(),
        #  }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            #user.profile_pic = self.cleaned_data["profile_pic"]
            user.save()
            teacher = Teacher.objects.create(user=user)
        return user
    
class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First Name','required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type':'email','placeholder':'Email','required': True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','placeholder':'Password','required': True}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','placeholder':'Password','required': True}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "first_name", "last_name")
        # widgets = {
        #  'photo': FileInput(),
        #  }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            #user.profile_pic = self.cleaned_data["profile_pic"]
            user.save()
            student = Student.objects.create(user=user)
            #student.profile_pic.add(*self.cleaned_data.get('profile_pic'))
        return user
    
class TeacherAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Email','required': True,'autofocus' : True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password','placeholder':'Password','required': True}))

