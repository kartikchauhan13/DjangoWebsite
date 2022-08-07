from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp,Testimonial
from .forms import FeedbackForm,EmpForm
# Create your views here.
def emp_home(request):

    emps=Emp.objects.all()
    return render(request, "emp/home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method=="POST":
        
        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")

        #validate

        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        #save the object
        e.save()
        #prepare msg
        
        return redirect("/emp/home/")
    form=EmpForm()
    
    return render(request, "emp/add_emp.html",{'form':form})


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request, "emp/update_emp.html",{
        'emp':emp
    })

def do_update_emp(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id") 
    
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp

        e.save()
    return redirect("/emp/home/")

def testimonials(request):
    testi=Testimonial.objects.all()

    return render(request, "emp/testimonials.html",{
        'testi':testi
    })


def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['email'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("data saved")
            return render(request,'emp/home.html')
        else:
            return render(request, "emp/feedback.html",{'form':form})
    else:
        form=FeedbackForm()
        return render(request, "emp/feedback.html",{'form':form})




