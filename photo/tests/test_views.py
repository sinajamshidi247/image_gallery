from django.test import TestCase , Client
from django.urls import reverse
from photo.models import Category , Photo
import json



class TestViews(TestCase):

    def setUp(self): # run per test before each one 
        category =Category.objects.create(name="sport")
        Photo.objects.create(name="test_sina",description="test test test",image="/home/sisil/Downloads/book.jpg")


    def tearDown(self):
        category =Category.objects.create(name="sport")
        photo = Photo.objects.get(name="test_sina",description="test test test",image="/home/sisil/Downloads/book.jpg")
        photo.delete()

    def test_home_get(self):
        client = Client()
        response = client.get(reverse('photo:home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response , 'photo/home.html')  # using for templates 


    def test_detail_get(self):
        client = Client()
        response = client.get(reverse('photo:detail',kwargs={'pk': 2}))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response , 'photo/detail.html')  # using for templates 


    def test_addphoto(self):
        client = Client()
        response = client.post(reverse('photo:add'),data={"name":"test_ali","category":1,"description":"test ali","image":"/home/sisil/Downloads/clothe.jpg"},follow=True) #1

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"photo/home.html") # redirect 
                                         


