from .models import Project
from rest_framework import viewsets, permissions
from .serializers import Project_serializers

class Project_view_set(viewsets.ModelViewSet):
    #metodo queryset
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] # cualquier usuario puede consultar con allowany
    serializer_class = Project_serializers
    
    