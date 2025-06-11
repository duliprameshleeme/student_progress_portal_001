from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')
    def __str__(self):
        return f"{self.name} ({self.course.name})"

