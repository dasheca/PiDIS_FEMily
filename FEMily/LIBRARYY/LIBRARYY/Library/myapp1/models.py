from django.db import models

class News(models.Model):
    name = models.CharField(max_length=20, blank=False)
    news = models.CharField(max_length=600, blank=False)

    def __str__(self):
        return f'{self.name} {self.news}'

class Books(models.Model):
    author = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=20, blank=False)
    photo = models.FileField()

    def __str__(self):
        return f'{self.author} {self.name}'
