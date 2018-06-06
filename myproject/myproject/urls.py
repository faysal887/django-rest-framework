from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
# from myapp.views import TaskViewSet, CreateUserView
from myapp import views
from myapp.views import (
	TaskDetailAPIView,
	TaskDeleteAPIView,
	TaskListAPIView,
	TaskUpdateAPIView,
	TaskCreateAPIView,
)

from rest_framework_simplejwt.views import (
	TokenRefreshView,
	TokenObtainPairView,
)

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	url(r'^$', 					  TaskListAPIView.as_view(),   name='list'),	
	url(r'^(?P<pk>\d+)/$',        TaskDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/edit/$',   TaskUpdateAPIView.as_view(), name='update'),
	url(r'^create/$',   		  TaskCreateAPIView.as_view(), name='create'),
	url(r'^(?P<pk>\d+)/delete/$', TaskDeleteAPIView.as_view(), name='delete'),
	url(r'^token/', TokenObtainPairView.as_view()),
	url(r'^token/refresh/', TokenRefreshView.as_view()),
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^admin/', admin.site.urls),
	url(r'^register/$', views.CreateUserView.as_view(), name='user'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)