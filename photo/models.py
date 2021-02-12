from django.db import models
from django.urls import reverse



class Category(models.Model):
    name= models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name_plural='categroies'


    def __str__(self):
        return self.name


    




class Photo(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='photo',on_delete=models.CASCADE,null=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='image/%Y/%m/%d/')

    

