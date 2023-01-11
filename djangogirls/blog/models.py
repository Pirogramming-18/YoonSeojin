from django.conf import settings
from django.db import models
from django.utils import timezone

#모델을 정의하는 코드 
#Post가 장고 모델임을 의미. 장고는 Post가 db에 저장되어야 한다고 알게 됨
class Post(models.Model):
    #속성 정의 시 필드마다 어떤 종류의 데이터 타입 가지는지 정하기
    # models.CharField = 글자 수가 제한된 텍스트 (글 제목)
    # models.TextField = 글자 수에 제한 없는 텍스트 (블로그 콘텐츠)
    # models.DateTimeField = 날짜와 시간
    # models.ForeignKey = 다른 모델에 대한 링크

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title