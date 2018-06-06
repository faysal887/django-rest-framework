from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
	task_name    = models.CharField(max_length=50)
	task_desc    = models.CharField(max_length=200)
	completed    = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now=True)
	# image 		 = models.ImageField(upload_to="Images/", default="Images/no_img.jpg", null=True, blank=True)

