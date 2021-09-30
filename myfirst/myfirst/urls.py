"""myfirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



# from myfirst.apps.users import views
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from django.apps import apps
from rest_framework import permissions



# urlpatterns = [
#     path('grappelli/', include('grappelli.urls')), 
#     path('articles/', include('adminPanel.urls')),
#     path('admin/', admin.site.urls)
#     path('api-auth/', include('rest_framework.urls'))
# ]



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class Office_MFCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=apps.get_model('users', 'Office_MFC')
        fields = [
            'id',
            'office_name',
            'addres',
            'phone_number'
        ]

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Office_MFCViewSet(viewsets.ModelViewSet):
    office = apps.get_model('users', 'Office_MFC')
    queryset = office.objects.all()
    serializer_class = Office_MFCSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = apps.get_model('organization', 'Organization')
        fields = (
            'id',
            'name',
            'activity'
        )

class Office_OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = apps.get_model('organization', 'Office_Organization')
        organizations = OrganizationSerializer(many=True, read_only=True)
        fields = (
            'id',
            'organization',
            'addres',
            'phone_number'
        )


class OrganizationViewSet(viewsets.ModelViewSet):
    organization = apps.get_model('organization', 'Organization')
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Office_OrganizationViewSet(viewsets.ModelViewSet):
    organization_office = apps.get_model('organization', 'Office_Organization')
    queryset = organization_office.objects.all()
    serializer_class = Office_OrganizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




# def Office_MFC_list(request):
    
#     if request.method == 'GET':
#         offices = Office_MFC.objects.all()
#         serializer = Office_MFCSerializer(offices, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = Office_MFCSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'clients', views.ClientViewSet)
router.register(r'offices', Office_MFCViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'organizations_office', Office_OrganizationViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('', include('api_basic.urls')),
    re_path(r'^grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    # path('', include('organization.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


