from django.http import HttpResponse
from django.shortcuts import render
from django. urls import path, include
from .import views
# Create your views here.

from django.shortcuts import render




# Create your views here.
def facultypagecall(request):
    return render(request,'facultyapp/FacultyHomePage.html')

def blogpagecall(request):
    return render(request,'facultyapp/blogpage.html')

#facultyapp/views.py
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import Task_Form, AddCourseForm, MarksForm
from .models import Task
def add_blog(request):
    if request.method == "POST":
        form = Task_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:add_blog')
    else:
        form = Task_Form()
    tasks = Task.objects.all()
    return render(request, 'facultyapp/blog_post.html', {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('facultyapp:add_blog')

from django.shortcuts import render

def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultyapp:FacultyHomePage')
    else:
        form = AddCourseForm()
    return render(request, 'facultyapp/AddCourse.html', {'form': form})

from .models import AddCourse
from adminapp.models import StudentList

def view_student_list(request):
    course = request.GET.get('course')
    section = request.GET.get('section')
    student_courses = AddCourse.objects.all()
    if course:
        student_courses = student_courses.filter(course=course)
    if section:
        student_courses = student_courses.filter(section=section)
    students = StudentList.objects.filter(id__in=student_courses.values('student_id'))
    course_choices = AddCourse.COURSE_CHOICES
    section_choices = AddCourse.SECTION_CHOICES
    context = {
        'students': students,
        'course_choices': course_choices,
        'section_choices': section_choices,
        'selected_course': course,
        'selected_section': section,
    }
    return render(request, 'facultyapp/view_student_list.html', context)


from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.http import HttpResponse
from django.shortcuts import render
from .forms import MarksForm

from django.core.mail import send_mail
from django.contrib.auth.models import User  # Assuming User is your custom user model
from .models import StudentList


def post_marks(request):
    if request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            marks_instance = form.save(commit=False)
            marks_instance.save()

            # Retrieve the User email based on the student in the form
            student = marks_instance.student
            student_user = student.user
            user_email = student_user.email

            subject = 'Marks Entered'
            message = f'Hello, {student_user.first_name}  marks for {marks_instance.course} have been entered. Marks: {marks_instance.marks}'
            from_email = 'gsrgc12@gmail.com'
            recipient_list = [user_email]
            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'facultyapp/marks_success.html')
    else:
        form = MarksForm()
    return render(request, 'facultyapp/post_marks.html', {'form': form})