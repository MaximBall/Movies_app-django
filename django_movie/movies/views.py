from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Actor, Genre


class Serach(View):
    def get(self, request):
        return render(request, "movies/movie_list.html")


class MoviesView(View):
    """Список фильмов"""
    #model = Movie
    #queryset = Movie.objects.filter(draft=False)
    #template_name = "movies/example.html"

    def get(self, request):
        movies = Movie.objects.all()
        directors = Actor.objects.all()
        genres = Genre.objects.all()

        return render(request, "movies/movie_list.html", {
            "movie_list": movies,
            "director_list": directors,
            "genres_list": genres,
            },
        )


class MovieDetailView(DetailView):
    """"Описание фильма"""
    """pk - некоторое число которое мы передаем из url"""
    model = Movie
    slug_field = "url"
    #queryset = Movie.objects.get(url=slug)
    #template_name = "movies/example.html"

    #def get(self, request, slug):
     #   movie = Movie.objects.get(url=slug)
      #  return render(request, "movies/movie_detail.html", {"movie": movie})