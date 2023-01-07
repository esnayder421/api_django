
# CREACION DE RUTAS 

from rest_framework import routers
from .api import Project_view_set

router = routers.DefaultRouter()

router.register('api/projects', Project_view_set, 'projects')
urlpatterns = router.urls
