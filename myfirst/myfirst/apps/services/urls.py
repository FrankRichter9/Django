from django.urls import include, path
from rest_framework import routers
from . import views



router = routers.DefaultRouter()
# router.register(r'serviceRendered', views.Service_renderedViewSet)
router.register(r'service', views.ServiceViewSet)
# router.register(r'documentation', views.DocumentationViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]