import time
from django.db import models

class WebStory(models.Model):
    id = models.AutoField(primary_key=True)
    permalink = models.CharField(max_length=255,unique=True)
    # cover_image = models.ImageField(upload_to="cover/",blank=True,)
    cover_url =  models.URLField()
    cover_text = models.TextField()
    cover_title = models.TextField()
    # cover_extension = models.TextField()

    def __str__(self):
        return self.cover_title

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    web_story = models.ForeignKey(WebStory, on_delete=models.CASCADE, related_name='images')
    text = models.TextField()
    # image = models.ImageField(upload_to= ("images/"),blank=True)
    image_url =  models.URLField()
    pos = models.PositiveSmallIntegerField()
    # extension = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.web_story} - {self.pos}"


def upload_to_location(instance, filename):
    return "images/{}".format(instance.image_title)

class AllImage(models.Model):
    image = models.ImageField(upload_to=upload_to_location)
    image_title = models.CharField(max_length=255)