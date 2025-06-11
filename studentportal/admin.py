from django.contrib import admin
from .models import Marks, Student
from .forms import MarksAdminForm

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course']    #name
    search_fields = ['name', 'email']

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    form = MarksAdminForm
    list_display = ['student', 'subject', 'assignment_marks', 'exam_marks']
    list_filter = ['student', 'subject']
    search_fields = ['student__name', 'subject__name']
