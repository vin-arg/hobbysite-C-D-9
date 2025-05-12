from django import forms
from .models import Commission, JobApplication, Job
from django.forms import inlineformset_factory

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []
        
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']
        
JobFormSet = inlineformset_factory(
    Job,
    form=JobForm,
    extra=2,
)