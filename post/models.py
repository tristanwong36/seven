# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=63, unique=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return(self.name)

class Post(models.Model):
    title = models.CharField(max_length=80)
    title_eng = models.CharField(max_length=80, blank=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='post')
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    description_eng = models.CharField(max_length=500, blank=True)
    pub_date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    text = models.CharField(max_length=10000)
    text_eng = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return(self.title)

    def get_absolute_url(self):
        return(reverse('readpost',
                       kwargs={'slug':self.slug}))
    
    def get_eng_url(self):
        return(reverse('readpost_eng',
                       kwargs={'slug':self.slug}))

class Subscriber(models.Model):
    LANG = (
        ('t', '瀪'),
        ('s', '简'),
        ('e', 'Eng'),)
    email = models.EmailField(unique=True)
    lang = models.CharField(max_length=3, choices=LANG)
    join_date = models.DateField(auto_now_add=True)
    



