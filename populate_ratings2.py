import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p006.settings')

import django
import csv, decimal, datetime

django.setup()

from showMovies.models import rating

def create_rating(user_id, content_id, ra, time):

    rate = rating(userId=(user_id*3), movieId=content_id, rate=decimal.Decimal(ra),
                    timestamp=datetime.datetime.fromtimestamp(float(time)))

    return rate


def delete_db():
    print('truncate db')
    rating.objects.all().delete()
    print('finished truncate db')

def populate(path):

    with open(path, newline='') as csvfile:
        rating_reader = csv.DictReader(csvfile, delimiter=',', skipinitialspace=True)
        ratings = []
        for rate in rating_reader:
            if len(rate) == 4:
                rate = create_rating(rate['userId'], rate['movieId'], rate['rating'], rate['timestamp'])
                ratings.append(rate)
            if len(ratings) == 1000:
                rating.objects.bulk_create(ratings)
                ratings = []
                print(".")
        rating.objects.bulk_create(ratings)
    print('database is populated with {} ratings'.format(rating.objects.count()))


if __name__ == '__main__':
    delete_db()
    populate('ratings.csv')