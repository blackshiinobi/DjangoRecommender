from django.contrib import admin
from .models import movie, rating, genre, UserInfo
# Register your models here.

admin.site.register(genre)
admin.site.register(movie)
admin.site.register(rating)
admin.site.register(UserInfo)