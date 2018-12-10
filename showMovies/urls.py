from django.urls import path
from . import views

app_name = 'showMovies'

urlpatterns = [
	path('', views.posterTest, name='Movie Posters'),
	path('info/<int:movie_id>/', views.details, name='Movie Details'),
	path('<str:genre_id>/', views.genrePage, name='Movie Genre'),
	path('movie/search/', views.movie_search, name='Movie Search'),
]