from django import forms
from lab1.models import Student


class BookForm(forms.Form):
    name = forms.CharField(max_length=50)
    author = forms.CharField(max_length=50)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone']


class DelStudentForm(forms.Form):
    pass
