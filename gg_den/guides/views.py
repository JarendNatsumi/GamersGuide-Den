from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import PostForm, RegisterForm
from .models import Post

def home(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED).select_related("author")
    kind = request.GET.get("type", "")
    if kind in ("guide", "review"):
        posts = posts.filter(post_type=kind)
    query = request.GET.get("q", "").strip()
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(game_name__icontains=query) |
                             Q(excerpt__icontains=query) | Q(content__icontains=query))
    page_obj = Paginator(posts, 9).get_page(request.GET.get("page"))
    return render(request, "guides/home.html", {"page_obj": page_obj, "kind": kind, "query": query})

def post_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related("author"), slug=slug)
    if post.status != Post.Status.PUBLISHED and not (request.user.is_authenticated and (request.user == post.author or request.user.is_staff)):
        raise Http404
    Post.objects.filter(pk=post.pk).update(views=F("views") + 1)
    post.refresh_from_db(fields=["views"])
    return render(request, "guides/post_detail.html", {"post": post})

def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Tài khoản đã được tạo. Chào mừng bạn đến GG Den!")
        return redirect("home")
    return render(request, "guides/register.html", {"form": form})

@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.success(request, "Bài viết đã được lưu.")
        return redirect(post.get_absolute_url() if post.status == Post.Status.PUBLISHED else "my_posts")
    return render(request, "guides/post_form.html", {"form": form, "heading": "Viết bài mới"})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Đã cập nhật bài viết.")
        return redirect(post.get_absolute_url() if post.status == Post.Status.PUBLISHED else "my_posts")
    return render(request, "guides/post_form.html", {"form": form, "heading": "Chỉnh sửa bài viết", "post": post})

@login_required
@require_POST
def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    post.delete()
    messages.success(request, "Đã xóa bài viết.")
    return redirect("my_posts")

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    page_obj = Paginator(posts, 12).get_page(request.GET.get("page"))
    return render(request, "guides/my_posts.html", {"page_obj": page_obj})
