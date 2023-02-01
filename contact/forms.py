from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    """
    A form for customers to send messages to store owner
    """

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
            'email': 'Enter your message here',
            'subject': 'Enter your your message subject',
            'message': 'Enter your message here',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'