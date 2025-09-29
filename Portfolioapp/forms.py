from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Authenticationapp.models import Profile
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_picture','address','city','country','postal_code','place','phone')

        help_texts = {
            'bio': 'Write a brief summary about yourself.',
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_title', 'project_description', 'project_imageone','project_imagetwo','project_imagethree','project_link',
                  'skillsone', 'skill_descriptionone', 'skillstwo', 'skill_descriptiontwo','skillsthree','skill_descriptionthree','skillsfour','skill_descriptionfour',
                  'company', 'role', 'duration','experience_description','institution', 'degree', 'course_duration','education_description','certification_name', 'issuing_institution', 'certification_year')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 30}),
        }



# fields = '__all__'


