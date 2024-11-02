from . import models, forms


def projecthomepage(request):
    return render(request ,'adminapp/ProjectHomePage.html')

# Create your views here.
def printpagecall(request):
    return render(request ,'adminapp/print_to_console.html')

def printpagelogic(request):
    if request.method == "POST":
        user_input =request.POST['user_input']
        print(f'User input: {user_input}')
    a1 = {'user_input': user_input}
    return render(request, 'adminapp/print_to_console.html', a1)


def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')


def exceptionpagelogic(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')


import random
import string


def randompagecall(request):
    return render(request, 'adminapp/RandomExample.html')


def randomlogic(request):
    if request.method == 'POST':
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran': ran}
    return render(request, 'adminapp/RandomExample.html', a1)


def calculator(request):
    return render(request, 'adminapp/calculator.html')


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm, StudentForm


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/AddTask.html', {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ProjectHomePage')  # Redirect to the home page or any other page
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'adminapp/loginpage.html')


def datetimepagecall(request):
    return render(request, 'adminapp/datetime.html')


from datetime import timedelta
import datetime


def datetimepagelogic(request):
    if request.method == "POST":
        number_of_days = int(request.POST.get('number_of_days', 0))  # Use get method with a default value
        current_date = datetime.datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
    else:
        future_date = None  # Initialize future_date to avoid UnboundLocalError
    context = {'future_date': future_date}
    return render(request, 'adminapp/datetime.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def registerpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'User registered successfully')
                return redirect('loginpage')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'adminapp/register.html')


from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render


def RegisterPageCall(request):
    return render(request, 'adminapp/register.html')


def RegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/loginpage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/loginpage.html')
    else:
        return render(request, 'adminapp/loginpage.html')

def logout(request):
    auth.logout(request)
    return redirect('ProjectHomePage')

# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm()
#     return render(request, 'adminapp/AddStudent.html', {'form': form})

from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/AddStudent.html', {'form': form})
            student.save()
            return redirect('student_list.html')
    else:
        form = StudentForm()
    return render(request, 'adminapp/AddStudent.html', {'form': form})


def add_studentpagecall(request):
    return render(request, 'adminapp/AddStudent.html')

from django.shortcuts import render
from .models import StudentList
def student_list(request):
    students = models.StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback

def feedback_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')

        feedback = Feedback(name=name, phone=phone, email=email, description=description)
        feedback.save()

        return render(request, 'adminapp/feedback_success.html')
    return render(request, 'adminapp/feedback.html')



from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ContactManager')
    else:
        form = ContactForm()
    contacts = Contact.objects.all()
    return render(request, 'adminapp/ContactManager.html', {'form': form, 'contacts': contacts})


def delete_Contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('add_contact')