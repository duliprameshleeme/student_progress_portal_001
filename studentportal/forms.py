from django import forms
from .models import Marks
from adminpanel.models import Subject

class MarksAdminForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MarksAdminForm, self).__init__(*args, **kwargs)
                                                # subject field need to all subjects 
        self.fields['subject'].queryset = Subject.objects.all()
