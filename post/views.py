# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



class Home(View):
    template = 'post/home.html'
    posts = Post.objects.all().order_by('pub_date')
    heading = posts[0]
    paginator = Paginator(posts[1:], 6)
    
    def get(self, request, lang=None):
        if not lang:
            template = self.template
        elif lang.lower() == 'en':
            template = 'post/home_eng.html'
        page_number = request.GET.get('page')
        try:
            page = self.paginator.page(page_number)
        except PageNotAnInteger:
            page = self.paginator.page(1)
        except EmptyPage:
            page = self.paginator.page(1)
        if page.has_previous():
            prev_url = '?page={}'.format(
                page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = '?page={}'.format(
                page.next_page_number())
        else:
            next_url = None
            
        return render(
            request,
            template,
            {'heading': self.heading,
             'page': page,
             'prev_url': prev_url,
             'next_url': next_url,
             'chinese': '\\',
             'eng': '\en'})


class ReadPost(View):
    def get(self, request, slug, lang=None):
        post = get_object_or_404(
            Post,
            slug=slug.lower())
        if not lang:
            template = 'post/articles/'+str(post.pub_date)+'-'+post.slug+'.html'
        elif lang.lower() == 'en':
            template = 'post/articles/'+str(post.pub_date)+'-'+post.slug+'_eng.html'
        post.views += 1
        post.save()
        return render(
            request,
            template,
            {'post': post,
             'eng': post.get_eng_url(),
             'chinese': post.get_absolute_url()})
