from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        label='Your name',
        required=True,
        error_messages={'required': 'What\'s your name?'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )
    contact_email = forms.EmailField(
        label='Your email',
        required=True,
        error_messages={'required': 'Please, inform your email'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'A valid one, please =P'
        })
    )
    contact_subject = forms.CharField(
        label='Subject',
        required=True,
        error_messages={'required': 'What is this message about?'},
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': ''
        })
    )
    contact_message = forms.CharField(
        label='Your message',
        required=True,
        error_messages={'required': 'A message is required to talk to me'},
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Talk to me'
        })
    )
