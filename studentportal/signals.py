from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student
from adminpanel.models import Subject

@receiver(post_save, sender=Student)
def assign_subjects_on_course_assignment(sender, instance, created, **kwargs):
    
    if instance.course:
        
        course_subjects = Subject.objects.filter(course=instance.course)


        pass
