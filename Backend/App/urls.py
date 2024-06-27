from django.urls import path
from App.views import *
urlpatterns = [
    path('', index, name='index'),
    path('project/<int:id>/', project_details, name='project_details'),
    path('create/project/', create_project, name='create_project'),
    path('delete/project/<int:id>/', delete_project, name="delete_project"),
    path('update/project/<int:id>/', update_project, name="update_project"),

    path('contact/', create_contact, name="create_contact"),
]
