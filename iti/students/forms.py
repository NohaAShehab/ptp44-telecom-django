
from django import forms
from students.models import Student
# you can use form to validate data
class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100
    )
    age = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    grade = forms.IntegerField()

    # define validation rule on any field
    def clean_email(self):
        email = self.cleaned_data['email']
        found = Student.objects.filter(email=email).exists()
        if found:
            raise forms.ValidationError("A student with this email already exists")

        return email

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) <3 or len(name) > 100:
            raise forms.ValidationError("Name must be between 3 and 100 characters")

        return name