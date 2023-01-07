from rest_framework import serializers
from .models import Project

class Project_serializers(serializers.ModelSerializer):  #esto serializers.ModelSerializer convirte los datos para que sean consultados 
    class Meta:
        model = Project
        fields =('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )