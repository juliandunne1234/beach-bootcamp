from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    """
    List admin user posts in order of posting
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'bootcamp_blog.html'


class PostDetail(View):
    """
    Select one of the posts to see approved user comments added to the post
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
            },
        )

    """
    Post comments to the selected blog post
    """
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm(),
            },
        )
