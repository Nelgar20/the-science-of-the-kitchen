from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm


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
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment is submitted and waiting for approval'
                )
    
    comment_form = CommentForm()

    return render(
        request,
        "blog/article_detail.html",
        {"article": article,
         "comments": comments,
         "comment_count": comment_count,
         "comment_form": comment_form,
         },
    )


def comment_edit(request, slug, comment_id):
    """
    Allows to edit comments
    """
    if request.method == "POST":

        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('article_detail', args=[slug]))