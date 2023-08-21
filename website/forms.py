from django import forms    
from website.models import Contact , Newsletter

class NameForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    massage = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject','email', 'message']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']