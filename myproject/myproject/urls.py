from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from myapp.views import TaskViewSet, CreateUserView
from myapp import views
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'task', views.TaskViewSet)
# router.register(r'completed_task', views.CompletedTaskViewSet)
# router.register(r'due_task', views.DueTaskViewSet)

urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^admin/', admin.site.urls),
	url(r'^', include(router.urls)),
	url(r'^register/$', views.CreateUserView.as_view(), name='user'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
