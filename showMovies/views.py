from django.shortcuts import render, redirect
from showMovies.models import movie, genre
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

def index(request):
	film = movie.objects.all()
	paginator = Paginator(film, 20)

	page = request.GET.get('page')

	m = paginator.get_page(page)

	api_key = "a8a96c562bbd8c7f6f192b5cefcf9c79"
	return render(request, 'showMovies/index.html', {'movies': m, 'api_key': api_key})


def posterTest(request):

	genre_selected = request.GET.get('genre')
	
	if genre_selected:
		selected = genre.objects.filter(name=genre_selected).first()
		film = selected.movies.order_by('-year', 'movieId')
	else:
		film = movie.objects.order_by('-year', 'movieId')

	#film = movie.objects.all()

	genres = genre.objects.all().values('name').distinct()

	paginator = Paginator(film, 20)
	page = request.GET.get('page')
	m = paginator.get_page(page)

	api_key = "a8a96c562bbd8c7f6f192b5cefcf9c79"

	context_dict = {'movies': m,
                    'genres': genres,
                    'api_key': api_key,
                    }

	return render(request, 'showMovies/posterTest.html', context_dict)


def details(request, movie_id):
	api_key = "a8a96c562bbd8c7f6f192b5cefcf9c79"
	genres = genre.objects.all().values('name').distinct()
	film = movie.objects.filter(movieId=movie_id).first()

	context_dict = {'title': film.title,
                    'genres': genres,
                    'api_key': api_key,
                    }

	return render(request, 'showMovies/movie.html', context_dict)


def genrePage(request, genre_id):

	if genre_id:
		selected = genre.objects.filter(name=genre_id).first()
		film = selected.movies.order_by('-year', 'movieId')
	else:
		film = movie.objects.order_by('-year', 'movieId')

	genres = genre.objects.all().values('name').distinct()

	paginator = Paginator(film, 20)
	page = request.GET.get('page')
	m = paginator.get_page(page)

	api_key = "a8a96c562bbd8c7f6f192b5cefcf9c79"

	context_dict = {'movies': m,
                    'genres': genres,
                    'api_key': api_key,
                    }

	return render(request, 'showMovies/posterTest.html', context_dict)


def movie_search(request):
	search_term = request.GET.get('movieQ', None)

	if search_term is None:
		return redirect('/posters/')

	film = movie.objects.filter(title__startswith=search_term)

	genres = genre.objects.all().values('name').distinct()
	api_key = "a8a96c562bbd8c7f6f192b5cefcf9c79"

	context_dict = {'movies': film.values(),
                    'genres': genres,
                    'api_key': api_key,
                    }

	return render(request, 'showMovies/movieResults.html', context_dict)