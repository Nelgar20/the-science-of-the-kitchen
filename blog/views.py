from django.shortcuts import render
from django.views import generic
from .models import Article


class ArticleList(generic.ListView):
    queryset = Article.objects.all()
    template = "article_list.html"
