"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import home, aboutPage, mycourses, enq, profile
from myapp.views import enquiries, editPage, deletePage, signup
from myapp.views import AddStudent, ViewStudent, EditStudent, DeleteStudent
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('about/',aboutPage,name='about'),
    path('course/',mycourses,name='courses'),
    path('enquiry/',enq,name='enq'),
    path('profile/',profile,name='staff'),

    path('profile/view/',enquiries,name='viewenq'),
    path('profile/view/edit/<id>/',editPage,name='editenq'),
    path('profile/view/delete/<id>/',deletePage,name='delenq'),

    path('profile/addStudent/',login_required(AddStudent.as_view()),name='addstu'),
    path('profile/viewStudent/',login_required(ViewStudent.as_view()),name='viewstu'),
    path('editStudent/<id>/',login_required(EditStudent.as_view()),name='editstu'),
    path('deleteStudent/<id>/',login_required(DeleteStudent.as_view()),name='delstu'),

    path('signup/',signup,name='signup'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('profile/logout/',LogoutView.as_view(next_page='home'),name='logout'),

    path('reset_password/',PasswordResetView.as_view(template_name='reset.html'),name='password_reset'),
    path('reset_done/',PasswordResetDoneView.as_view(template_name='reset_done.html'),name='password_reset_done'),
    path('reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='confirm.html'),name='password_reset_confirm'),
    path('reset_complete/',PasswordResetCompleteView.as_view(template_name='complete.html'),name='password_reset_complete')


]
