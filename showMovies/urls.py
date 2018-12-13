from django.urls import path
from . import views

app_name = 'showMovies'

urlpatterns = [
	path('', views.posterTest, name='Movie Posters'),
	path('register/', views.register, name='Registration Page'),
	path('info/<int:movie_id>/', views.details, name='Movie Details'),
	path('info/<int:movie_id>/rate', views.rate, name='Movie Rate'),
	path('genre/<str:genre_id>/', views.genrePage, name='Movie Genre'),
	path('movie/search/', views.movie_search, name='Movie Search'),
]