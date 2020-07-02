from django import forms  
from .models import Student, Result 
 
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__"  

class ResultForm(forms.ModelForm):
	class Meta:
		model = Result
		fields = "__all__"