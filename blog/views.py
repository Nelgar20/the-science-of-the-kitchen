from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Article


class ArticleList(generic.ListView):
    queryset = Article.objects.filter(status=1)
    template = "article_list.html"
    paginate_by = 6


def article_detail(request, slug):
    """
    Display an individual :model:`blog.Article`.

    **Context**

    ``article``
        An instance of :model:`blog.Article`.

    **Template:**

    :template:`blog/article_detail.html`
    """

    queryset = Article.objects.filter(status=1)
    article = get_object_or_404(queryset, slug=slug)
    comments = article.comments.all().order_by("-created_on")
    comment_count = article.comments.filter(approved=True).count()

    return render(
        request,
        "blog/article_detail.html",
        {"article": article,
         "comments": comments,
         "comment_count": comment_count,},
    )