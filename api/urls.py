

from django.urls import path
from . import views
#from django.urls import path, include
#from rest_framework import routers

#router = routers.DefaultRouter()

urlpatterns = [
    #path('', include(router.urls)),
    #path('',views.apiOverview, name='apiOverview'),
    path('book-list/', views.showAll, name='book-list'),  #changed function initial to lower case
    path('book-detail/<int:pk>/', views.viewBook, name='book-detail'),#changed function initial to lower case
    path('book-create/', views.createBook, name='book-create'),#changed function initial to lower casegit
    path('book-update/<int:pk>/', views.updateBook, name='book-update'),
    path('book-delete/<int:pk>/', views.deleteBook, name='book-delete'),
    

]
