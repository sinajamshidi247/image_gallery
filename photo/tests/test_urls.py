from django.test import SimpleTestCase
#simpletest case use when we dont need to use database fore testing
from django.urls import reverse , resolve 
from photo.views import home  , detail , addPhoto # views that urls(home) path to this one
from photo.models import Photo 
import re




class TestUrls(SimpleTestCase):

    def test_home(self): # name of first url of photo app 

        url = reverse('photo:home') # must be write app name
        # print(resolve(url)) resolve return function for each url's name 
        self.assertEquals(resolve(url).func,home)

    def test_detail(self):
        url  = reverse('photo:detail',kwargs={'pk':3})
        # print(resolve(url))
        self.assertEquals(resolve(url).func,detail)


    def test_add(self):
        url = reverse("photo:add")
        self.assertEquals(resolve(url).func,addPhoto)


