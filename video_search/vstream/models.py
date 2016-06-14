from django.db import models


class Videoinfo(models.Model):
    name = models.TextField(max_length=1000)
    url = models.TextField(max_length=1000)
    description = models.TextField(max_length=500,null=True)
    videodate = models.DateField(null=True)
