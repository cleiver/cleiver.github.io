from urllib.parse import unquote

from django.contrib import messages
from django.core import mail
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

from resume.forms import ContactForm


def index(request):
    return render(request, 'resume/index.html')


def about(request):
    return render(request, 'resume/about.html')


def contact(request):
    form = ContactForm()

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data
            contact_name = cd.get('contact_name', '')
            contact_email = cd.get('contact_email', '')
            contact_subject = cd.get('contact_subject', '')
            contact_message = cd.get('contact_message', '')

            connection = mail.get_connection()
            connection.open()
            email = EmailMessage('[cleiver.com] ' + contact_subject,
                                 contact_name + ' escreveu:\n---\n' + contact_message,
                                 'contact@cleiver.com',
                                 ['contact@cleiver.com'],
                                 connection=connection,
                                 headers={'Reply-To': contact_email}
                                 )

            if email.send():
                messages.success(request, 'Message sent! \O/ Thank you, {}!'.format(contact_name))

            else:
                messages.error(request, 'Errr... something happened :( Please try again later or send me an email '
                                        'directly to ' + unquote(
                    '%63%6C%65%69%76%65%72%40%67%6D%61%69%6C%2E%63%6F%6D'))

            connection.close()

    return render(request, 'resume/contact.html', {'form': form})


def experience(request):
    return render(request, 'resume/experience.html')


def education(request):
    return render(request, 'resume/education.html')
