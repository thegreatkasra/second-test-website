from django import forms
from website.models import Contact , Newsletter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    massage = forms.CharField(widget=forms.Textarea)
    
class ContactForm(forms.ModelForm):
    subject = forms.CharField(required=False)
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'subject','email', 'message']

        def clean_name(self):
            return 'unknown'
           
    
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']

