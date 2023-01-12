from django.conf import settings
from django.db import models
from django.utils import timezone


class MovieReview(models.Model):
    #영화제목 / 개봉 년도 / 장르 / 별점
    title = models.CharField(max_length = 200)
    released = models.IntegerField()
    genre = models.CharField(max_length = 200)
    star = models.FloatField()

    