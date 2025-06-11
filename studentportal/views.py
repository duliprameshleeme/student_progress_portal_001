from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Student, Marks  

def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("student_dashboard")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "studentportal/login.html")  # GET request => show login page

def student_logout(request):
    logout(request)
    return redirect('student_login')  # logout වෙලා login page එකට යනවා

def student_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('student_login')

    try:
        student = Student.objects.get(user=request.user)
        marks = Marks.objects.filter(student=student)

        # Average calculation
        if marks.exists():
            average = sum([m.total for m in marks]) / marks.count()
        else:
            average = 0

        
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "F"

        context = {
            'student': student,
            'marks': marks,
            'average': round(average, 2),
            'grade': grade,
        }
        return render(request, 'studentportal/dashboard.html', context)

    except Student.DoesNotExist:
        return render(request, 'studentportal/dashboard.html', {'error': 'Student profile not found'})

