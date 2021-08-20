from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WebPage(models.Model):
    title = models.CharField(max_length=50)
    fa_icon = models.CharField(max_length=100, default="")
    url = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title


class WebPageSection(models.Model):
    webpage = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'page: {self.webpage} | Section: {self.title}'


class WebpageContent(models.Model):
    webpagesection = models.ForeignKey(WebPageSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    fontaweomeicons_one = models.CharField(max_length=200, blank=True)
    #fontaweomeicons_content_one = models.CharField(max_length=200, blank=True)
    fontaweomeicons_two = models.CharField(max_length=200, blank=True)
    #fontaweomeicons_content_two = models.CharField(max_length=200, blank=True)
    fontaweomeicons_three = models.CharField(max_length=200, blank=True)
   # fontaweomeicons_content_three = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=5000, blank=True)
    image = models.ImageField(default="default.png", upload_to="upload_images")
    url = models.CharField(max_length=150, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title