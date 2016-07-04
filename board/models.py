from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

class Thread(models.Model):
	thread_title = models.CharField(max_length=80, blank=True, default='')
	thread_text = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.thread_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Comment(models.Model):
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	author = models.CharField(max_length=25, blank=True, default='')
	comment_text = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.comment_text
