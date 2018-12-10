from django.db import models

# Create your models here.
class genre(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name

class movie(models.Model):
	movieId = models.CharField(max_length=16, primary_key=True, db_column='movieId')
	title = models.CharField(max_length=128)
	year = models.IntegerField(null=True)
	genres = models.ManyToManyField(genre, related_name='movies', db_table='movie_genre')

	def __str__(self):
		return self.title

class rating(models.Model):
	userId = models.CharField(max_length=16)
	movieId = models.ForeignKey(movie, on_delete=models.CASCADE)
	rate = models.CharField(max_length=300)
	timestamp = models.CharField(max_length=300) 