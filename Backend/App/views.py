from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from App.Serializer import ProjectSerealizer, ContactSerializer
from App.models import Project

from App.helpers.email_helper import mail_send

# Ultimately move the crud functionality into one function for projects


@api_view(['GET'])
def index(request):
    query = Project.objects.all()
    Serializer = ProjectSerealizer(query, many=True)
    return Response(Serializer.data)


@api_view(['GET'])
def project_details(request, id):
    project = get_object_or_404(Project, id=id)
    Serializer = ProjectSerealizer(project)
    return Response(Serializer.data)


@api_view(['POST'])
def create_project(request):
    # the tags are passed to the validated_data for the sereializer so it can be added to the project_insctance
    req = request.data
    tags = req.get('tags', [])  # get the 'tags' from the api request (1)
    Serializer = ProjectSerealizer(data=request.data)
    if Serializer.is_valid():
        Serializer.save(tags=tags)  # passing tags to validated_data (2)
        return Response(Serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def update_project(request, id):
    req = request.data
    tags = req.get('tags', [])  # getting tags
    project = get_object_or_404(Project, id=id)
    print(project)
    serializer = ProjectSerealizer(project, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save(tags=tags)  # passing it to serializer's validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_project(request, id):
    project_instance = get_object_or_404(Project, id=id)
    project_name = project_instance.title
    project_instance.delete()
    return Response({"Message": f"{project_name} deleted"})


@api_view(["POST"])
def create_contact(request):
    serializer = ContactSerializer(data=request.data)
    email = request.data.get('email')
    name = request.data.get('name')
    # print(serializer)

    if serializer.is_valid():
        serializer.save()
        # move the sending of emails to background task , like celery
        # mail_send(email, name)
        # (WITHOUT CELERY AVG TIME TO SEND MAIL = 3.8s )
        # i want to send mail from sameerahmedjan00@gmail.com TO the email i recive in the contact submition
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
