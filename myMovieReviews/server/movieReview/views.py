from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from .models import MovieReview, MovieDetail

def movie_list(request) :
    movies = MovieReview.objects.all()
    text = request.GET.get("text")
    if text:
        movies = movies.filter(content__contains=text)
    return render(request, 'movieReview/movie_list.html', {"movies": movies})

def movie_detail(request:HttpRequest, pk, *args, **kwargs):
    movie = MovieDetail.objects.all().get(id=pk)
    return render(request, "movieReview/movie_detail.html", {'movie':movie})


def movie_create(request: HttpRequest, *args, **kwargs):
    if request.method == "POST":
        MovieDetail.objects.create(
            title=request.POST["title"],
            director=request.POST["director"],
            cast=request.POST["cast"],
            genre=request.POST["genre"],
            star=request.POST["star"],
            runtime=request.POST["runtime"],
            review=request.POST["review"],
        )
        return redirect("/")
    return render(request, 'movieReview/movie_create.html')