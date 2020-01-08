"""gabinetLaryngologii URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import include, path
from rest_framework import routers
from gabinetLaryngologii.blog import views as viewsBlog
from gabinetLaryngologii.material import views as viewsMaterial
from gabinetLaryngologii.contact import views as viewsContact
from gabinetLaryngologii.visit import views as viewsVisit
from django.contrib import admin

router = routers.DefaultRouter()
# router.register(r'users', viewsBlog.UserViewSet)
# router.register(r'groups', viewsBlog.GroupViewSet)
router.register(r'posts', viewsBlog.PostViewSet)
router.register(r'media', viewsMaterial.MediaViewSet)
router.register(r'visits', viewsVisit.AppointmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('contact/', viewsContact.ContactView.as_view())


]
