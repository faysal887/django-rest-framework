from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers, UserSerializer
from .models import Task
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


@permission_classes((IsAuthenticated,))
class TaskViewSet(viewsets.ModelViewSet):
	# permission_classes = (IsAuthenticated,)

	queryset = Task.objects.all().order_by('-date_created')
	serializer_class = TaskSerializers

	filter_backends = (DjangoFilterBackend, OrderingFilter)
	filter_fields = ('completed',)
	ordering = ('-date_created',)


class CreateUserView(CreateAPIView):
	model = get_user_model()
	permission_classes = (AllowAny, )
	serializer_class = UserSerializer

# class DueTaskViewSet(viewsets.ModelViewSet):
# 	queryset = Task.objects.filter(completed=False).order_by('-date_created')
# 	serializer_class = TaskSerializers


# class CompletedTaskViewSet(viewsets.ModelViewSet):
# 	queryset = Task.objects.filter(completed=True).order_by('-date_created')
# 	serializer_class = TaskSerializers

