from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, label="Email")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {"username": "Tên tài khoản", "password1": "Mật khẩu", "password2": "Nhập lại mật khẩu"}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("post_type", "title", "game_name", "excerpt", "content", "cover", "status")
        widgets = {
            "excerpt": forms.Textarea(attrs={"rows": 2}),
            "content": forms.Textarea(attrs={"rows": 14, "placeholder": "Chia sẻ cách chơi, chiến thuật, mẹo hoặc đánh giá của bạn..."}),
        }
        labels = {"post_type": "Loại bài", "title": "Tiêu đề", "game_name": "Tên game",
                  "excerpt": "Tóm tắt", "content": "Nội dung", "cover": "Ảnh bìa",
                  "status": "Trạng thái"}
