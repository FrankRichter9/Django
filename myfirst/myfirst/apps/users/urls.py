from django.urls import include, path
from rest_framework import routers
from . import views
from views import Office_MFC_list

router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'office_mfc', views.Office_MFCViewSet)



urlpatterns = [
    # path('offices/', Office_MFC_list),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]