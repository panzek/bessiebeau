from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """
    A form for customers to send messages to store owner
    """

    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'message',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Enter your name here',
            'email': 'Enter your message here',
            'subject': 'Enter your your message subject',
            'message': 'Enter your message here',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'