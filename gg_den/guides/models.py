from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    class PostType(models.TextChoices):
        GUIDE = "guide", "Guide"
        REVIEW = "review", "Review"
    class Status(models.TextChoices):
        DRAFT = "draft", "Bản nháp"
        PUBLISHED = "published", "Đã xuất bản"

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="game_posts")
    post_type = models.CharField("Loại bài", max_length=10, choices=PostType.choices, default=PostType.GUIDE)
    title = models.CharField("Tiêu đề", max_length=180)
    slug = models.SlugField(max_length=200, blank=True)
    game_name = models.CharField("Tên game", max_length=100, blank=True)
    excerpt = models.CharField("Tóm tắt", max_length=280)
    content = models.TextField("Nội dung")
    cover = models.ImageField("Ảnh bìa", upload_to="covers/", blank=True, null=True)
    status = models.CharField("Trạng thái", max_length=12, choices=Status.choices, default=Status.PUBLISHED)
    created_at = models.DateTimeField("Ngày tạo", auto_now_add=True)
    updated_at = models.DateTimeField("Cập nhật", auto_now=True)
    views = models.PositiveIntegerField("Lượt xem", default=0)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "bài viết"
        verbose_name_plural = "bài viết"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:180] or "game-post"
            candidate, n = base, 2
            while Post.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                candidate = f"{base}-{n}"
                n += 1
            self.slug = candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
