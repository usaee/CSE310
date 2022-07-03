from django.db import models


class TodoItem(models.Model):
    content = models.TextField()


class TodoHistory(models.Model):
    hist_content = models.TextField()





