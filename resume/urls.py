from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    # /
    path('', views.contact, name='main-page'),
    # /experience
    path('experience', views.experience, name='experience-page'),
    # /education
    path('education', views.education, name='education-page'),
    # /contact
    path('contact', views.contact, name='contact-page'),
]
