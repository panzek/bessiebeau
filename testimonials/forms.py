from django import forms
from testimonials.models import Testimonial


class TestimonialForm(forms.ModelForm):
    """
    A form for customers to write their testimonial
    """

    class Meta:
        model = Testimonial
        fields = (
            'name',
            'email',
            'body',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Your name',
            'email': 'Email Address',
            'body': 'Write your testimonial',
        }

        self.fields['email'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control'