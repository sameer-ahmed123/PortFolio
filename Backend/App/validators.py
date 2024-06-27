from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from App.models import *

# def validate_title(self, value):
#         # request = self.context.get('request')
#         # user = request.user
#         # qs=Project.objects.filter(user=user , title__iexact=value)
#         qs = Project.objects.filter(title__iexact=value)
#         if qs.exists():
#             raise serializers.ValidationError({f"{value} already exists"})
#         return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError({f"{value} is not allowed"})
    return value


unique_project_title = UniqueValidator(queryset=Project.objects.all())

def validate_contact_email(value):
    if "fuck" in value.lower():
        raise serializers.ValidationError(f"profanity not allowed")

    return value
