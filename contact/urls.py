from django.urls import path
from . import views
app_name = 'contact'
urlpatterns = [
    path('', views.ContactForm.as_view(), name='contact'),
    path('postEmail/', views.postEmail, name='postEmail'),
]
