from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models

# Create your models here.

"""
게시판 기능
- 제목(20글자이내)
- 내용(긴 글)
- 글 작성시간/수정시간(자동으로기록, 날짜/시간)
- 이미지 업로드기능
"""


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )  # saved to 'MEDIA_ROOT/images'
