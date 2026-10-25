from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("bai-viet/<slug:slug>/", views.post_detail, name="post_detail"),
    path("viet-bai/", views.post_create, name="post_create"),
    path("bai-viet/<slug:slug>/sua/", views.post_edit, name="post_edit"),
    path("bai-viet/<slug:slug>/xoa/", views.post_delete, name="post_delete"),
    path("dang-ky/", views.register, name="register"),
    path("dang-nhap/", auth_views.LoginView.as_view(template_name="guides/login.html"), name="login"),
    path("dang-xuat/", auth_views.LogoutView.as_view(), name="logout"),
    path("tai-khoan/bai-viet/", views.my_posts, name="my_posts"),
]
