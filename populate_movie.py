import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p006.settings')

django.setup()
from showMovies.models import movie, genre

csv_filepathname="movies.csv"

dataReader = csv.reader(open(csv_filepathname, encoding="utf8"), delimiter=',', quotechar='"')

#movie.objects.all().delete()
#genre.objects.all().delete()

for row in dataReader:
	film = movie()
	film.movieId = row[0]
	title_year = row[1].split(sep="(")
	film.title = title_year[0]
	film_year1 = title_year[len(title_year)-1].split(sep=")")
	film.year = film_year1[0]
	film.save()
	for gen in row[2].split(sep="|"):
		g =  genre.objects.get_or_create(name=gen)[0]
		film.genres.add(g)
		g.save()
	film.save()