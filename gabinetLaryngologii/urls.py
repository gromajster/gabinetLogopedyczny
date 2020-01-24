from django.urls import include, path
from rest_framework import routers
from gabinetLaryngologii.blog import views as viewsBlog
from gabinetLaryngologii.material import views as viewsMaterial
from gabinetLaryngologii.contact import views as viewsContact
from gabinetLaryngologii.visit import views as viewsVisit
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'posts', viewsBlog.PostViewSet)
router.register(r'media', viewsMaterial.MediaViewSet)
router.register(r'visits', viewsVisit.AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('contact/', viewsContact.ContactView.as_view()),
]
