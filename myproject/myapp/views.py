from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model

from .serializers import (
	TaskDetailSerializers,	
	TaskListSerializers, 
	UserSerializer
)

from django_filters.rest_framework import (
	DjangoFilterBackend, 
	FilterSet
)

from rest_framework.decorators import (
	api_view, 
	authentication_classes,
	permission_classes
)

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	CreateAPIView
)

class TaskCreateAPIView(CreateAPIView):
	serializer_class = TaskDetailSerializers

class TaskListAPIView(ListAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskListSerializers

class TaskDetailAPIView(RetrieveAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskDetailSerializers

class TaskUpdateAPIView(UpdateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskDetailSerializers


class TaskDeleteAPIView(DestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskDetailSerializers

@permission_classes((AllowAny,))
class CreateUserView(CreateAPIView):
	model = get_user_model()
	serializer_class = UserSerializer



