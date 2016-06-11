from django.db import models


class video_info(models.Model):
    name = models.CharField(max_length=30)
    url= models.CharField(max_length=30)
    description =models.CharField(max_length=500)
    videodate = models.DateField(null =True)
