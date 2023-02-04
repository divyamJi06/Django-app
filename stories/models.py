import time
from django.db import models
from django.core.files import File
from tempfile import NamedTemporaryFile
from urllib.request import urlopen

class WebStory(models.Model):
    id = models.AutoField(primary_key=True)
    permalink = models.CharField(max_length=255,unique=True)
    # cover_image = models.ImageField(upload_to="cover/",blank=True,)
    cover_url =  models.URLField()
    cover_text = models.TextField()
    cover_title = models.TextField()
    # cover_extension = models.TextField()


    # def save(self, *args, **kwargs):
    #     #    def save(self, *args, **kwargs):
    #     if self.cover_url and not self.cover_image:
    #         img_temp = NamedTemporaryFile(delete=True)
    #         img_temp.write(urlopen(self.cover_url).read())
    #         img_temp.flush()
    #         self.cover_image.save(f"image_{self.cover_extension}", File(img_temp))
        
    #     super(WebStory, self).save(*args, **kwargs)

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

