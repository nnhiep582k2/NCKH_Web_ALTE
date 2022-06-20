from django.urls import path
from . import views

app_name = 'properties'
urlpatterns = [
    # properties
    path('', views.getProperty, name='getProperties'),
    path('postProperties/', views.postProperty, name='postProperties'),
    
    # favorites
    path('favoritesList/', views.getfavoritesList, name='getFavoritesList'),
    path('favoritesList/postFavoritesList',views.postProperty, name='postFavoritesList'),
    
    # search
    path('searchList/', views.getSearchList, name='getSearch'),
    path('postSearchList/', views.postSearchList, name='postSearchList'),
    
    path('like/', views.like_user, name='like-user'),
    
    # Details
    path('<int:id>/',views.Details_house, name='getDetails'),
    path('Details/postDetails/',views.PostDetails_house, name='postDetails'),
    
    path('<int:id>/',views.SubDetails_house, name='SubDetails'),
    
]
