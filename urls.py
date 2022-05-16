
from .import views
from django.urls import path

urlpatterns = [
   
    path('', views.home , name='home'),
    path('login/', views.login , name='login'),
    path('signup/', views.signup , name='signup'),
    path('logout/', views.signout , name='logout'),
    path('add-todo/', views.Addtodo , name='add_todo'),
    path('delete-todo/<int:id>', views.delete_todo , name='delete_todo'),
    path('change-status/<int:id>/<str:status>', views.Change_status , name='change-todo-status'),
]
