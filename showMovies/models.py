from django.db import models
from django.contrib.auth.models import User

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
	movieId = models.CharField(max_length=16)
	rate = models.DecimalField(decimal_places=2, max_digits=4)
	timestamp = models.DateTimeField()

	def __str__(self):
		return "userId: {}, movieId: {}, rating: {}".format(self.userId, self.movieId, self.rate)

class UserInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username