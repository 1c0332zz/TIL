from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.order_by("-pk")
    context = {
        "movies": movies,
    }
    return render(request, "movies/index.html", context)


def create(request):
    if request.method == "POST":
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movies:index")
    else:
        movie_form = MovieForm()
    context = {
        "movie_form": movie_form,
    }
    return render(request, "movies/new.html", context=context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        movie_form = MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect("movies:detail", movie.pk)
    else:
        movie_form = MovieForm(instance=movie)
    context = {
        "movie_form": movie_form,
    }
    return render(request, "movies/update.html", context=context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        "movie": movie,
    }
    return render(request, "movies/detail.html", context)


def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect("movies:index")
