from django.db import models

class Task(models.Model):
    """Basic cron jobs monitoring"""
    name = models.CharField(max_length=40)
    last_execution = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
