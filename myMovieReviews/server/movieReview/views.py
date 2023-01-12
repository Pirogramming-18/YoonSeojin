from django.shortcuts import render
from .models import MovieReview

def movie_list(request) :
    movies = MovieReview.objects.all()
    text = request.GET.get("text")
    if text:
        movies = movies.filter(content__contains=text)
    return render(request, 'movieReview/movie_list.html', {"movies": movies})