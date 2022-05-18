from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.homeIndex.as_view(),name='home'),
    path('create/', views.create,name='create'),
]

