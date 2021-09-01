

from django.urls import path
from . import views
#from django.urls import path, include
#from rest_framework import routers

#router = routers.DefaultRouter()

urlpatterns = [
    #path('', include(router.urls)),
    #path('',views.apiOverview, name='apiOverview'),
    path('book-list/', views.ShowAll, name='book-list'),
    path('book-detail/<int:pk>/', views.ViewBook, name='book-detail'),
    path('book-create/', views.CreateBook, name='book-create'),
    path('book-update/<int:pk>/', views.updateBook, name='book-update'),
    path('book-delete/<int:pk>/', views.deleteBook, name='book-delete'),
    

]
