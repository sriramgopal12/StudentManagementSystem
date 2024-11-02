from django.urls import path, include
from . import views
from .views import datetimepagecall

urlpatterns =[
    path('', views.projecthomepage, name='ProjectHomePage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randompagecall/',views.randompagecall,name='randompagecall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('calculator/',views.calculator,name='calculator'),
    path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
    path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
    path('RegisterPageCall/',views.RegisterPageCall,name='RegisterPageCall'),
    path('RegisterLogic/',views.RegisterLogic,name='RegisterLogic'),
    path('logout/',views.logout,name='logout'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('add_student/',views.add_student,name='add_student'),
    path('add_studentpagecall/',views.add_studentpagecall,name='add_studentpagecall'),
    path('student_list/',views.student_list,name='student_list'),
    path('submit_feedback', views.feedback_form, name='submit_feedback'),
    path('add_contact',views.add_contact,name='add_contact'),
    path('contact_manager/', views.add_contact, name='ContactManager'),
    path('delete_contact/<int:pk>/', views.delete_Contact, name='delete_Contact'),
]

