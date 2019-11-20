from django.db import models
from django.conf import settings

# admin.py 에 모델 등록할 것.
class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=140)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_movies')


class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    # 1:N 관계는 ForeignKey, M:N 은 ManyToMany
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
    related_name="reviews", 
    on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)