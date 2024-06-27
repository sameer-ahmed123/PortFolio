from rest_framework import serializers
from App.models import *
from taggit.models import Tag
from App.validators import validate_title_no_hello, unique_project_title, validate_contact_email


class TagSearealizer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class ProjectSerealizer(serializers.ModelSerializer):
    proj_tags = TagSearealizer(many=True, read_only=True, source='tags')
    title = serializers.CharField(
        validators=[validate_title_no_hello, unique_project_title])
    name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'type',
            'url',
            'proj_tags',
            'name'
        ]

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        project_instance = Project.objects.create(**validated_data)
        for tag_data in tags:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            project_instance.tags.add(tag)
        return project_instance

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.url = validated_data.get('url', instance.url)

        instance.tags.clear()  # clear tags associated with instance

        for tag_data in tags:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            instance.tags.add(tag)
        instance.save()  # save changes
        return instance


class ContactSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_contact_email])

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]
