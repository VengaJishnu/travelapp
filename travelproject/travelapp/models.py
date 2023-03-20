from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name
        #to call all the model in name wise (in admin panel)


class assignment(models.Model):
    name_1 = models.CharField(max_length=100)
    img_1 = models.ImageField(upload_to='pics')
    desc_1 = models.TextField()

    def __str__(self):
        return self.name_1