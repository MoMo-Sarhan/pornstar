from django.db import models
import json

# Create your models here.

class Pornstar(models.Model):
    name = models.CharField(max_length=30)
    image_link=models.ImageField(upload_to='photo/%y/%m/%d')
    age = models.IntegerField()
    height= models.IntegerField()
    eye_color=models.CharField(max_length=50)
    hair_color=models.CharField(max_length=50)
    sex=models.CharField(max_length=50)
    catigories=models.TextField(null=True,blank=True)
    relative_catigories= models.CharField(max_length=255)
    isalive=models.BooleanField(default=True)
    def set_list(self,lst):
        self.catigories=json.dumps(lst)
    def get_list(self):
        return json.loads(self.catigories)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "pornstar"
        ordering=['name']