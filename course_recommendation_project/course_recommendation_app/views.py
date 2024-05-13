from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from.models import User, Course, CourseKeyword

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html', {'user': request.user})
    else:
        return redirect('login')

def recommend_courses(request):
    if request.user.is_authenticated:
        # Implement your course recommendation logic here
        top_courses = Course.objects.all()[:4]  # Simplified example
        return render(request, 'recommendations.html', {'courses': top_courses})
    else:
        return redirect('login')

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Implement logic to display course details and collect attention metrics
    return render(request, 'course_detail.html', {'course': course})

def attention_metrics(request):
    # Implement logic to display collected attention metrics
    return render(request, 'attention_metrics.html')
