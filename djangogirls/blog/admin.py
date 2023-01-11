from django.contrib import admin
from .models import Post

#관리자 페이지에서 만들 모델을 보기 위해 아래 코드로 모델 등록
admin.site.register(Post)
