from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from datetime import datetime
from myapp.forms import EnquiryForm, SignupForm
from myapp.models import Enquiry, Student
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request,'base.html')

def aboutPage(request):
    current_time = datetime.now()
    return render(request,'about.html',{'time':current_time,'name':'paviThRa','place':'cHenNaI tamil nadu'})

def mycourses(request):
    return render(request,'courses.html')

def enq(request):
    obj = EnquiryForm(request.POST or None)
    if obj.is_valid():
        obj.save()
        return HttpResponse("Saved Successfully!")
    return render(request,'enquiryform.html',{'myform':obj})

@login_required()
def profile(request):
    return render(request,'profile.html')

@login_required()
def enquiries(request):
    data = Enquiry.objects.all()
    return render(request,'enquiries.html',{'enq':data})

@login_required()
def editPage(request, id):
    data = get_object_or_404(Enquiry, pk=id)
    form = EnquiryForm(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        #return HttpResponse("Updated Successfully!")
        return redirect('/profile/view')
    return render(request,'updateEnquiry.html',{'data':form})

@login_required()
def deletePage(request,id):
    data = get_object_or_404(Enquiry,pk=id)
    #data.delete()
    #return HttpResponse('Deleted Successfully!')
    #return redirect('/profile/view')
    if request.method == "POST":
        data.delete()
        return redirect('/profile/view')
    return render(request,'delete.html',{'data':data})


class AddStudent(CreateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy('staff')
    template_name = 'addStudent.html'

class ViewStudent(ListView):
    model = Student
    template_name = 'viewStudents.html'
    context_object_name = 'students'

class EditStudent(UpdateView):
    model = Student
    fields = ('stdName','course','fees','phone','email','address','joiningDate','gender','status')
    template_name = 'editStudent.html'
    success_url = reverse_lazy('viewstu')

    def get_object(self, queryset=None):
        obj = get_object_or_404(Student,stdId=self.kwargs['id'])
        return obj

class DeleteStudent(DeleteView):
    model = Student
    template_name = 'deleteStudent.html'
    success_url = reverse_lazy('viewstu')

    def get_object(self, queryset=None):
        obj = get_object_or_404(Student,stdId=self.kwargs['id'])
        return obj


def signup(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Account Created Successfully!")
    return render(request,'signup.html',{'form':form})