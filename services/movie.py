from django.db import transaction
from db.models import Movie


def get_movies(genres_ids=None, actors_ids=None, title=None):
    qs = Movie.objects.all()

    if genres_ids:
        qs = qs.filter(genres__id__in=genres_ids)

    if actors_ids:
        qs = qs.filter(actors__id__in=actors_ids)

    if title:
        qs = qs.filter(title__icontains=title)

    return qs


def get_movie_by_id(movie_id):
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title, movie_description, genres_ids=None, actors_ids=None):
    with transaction.atomic():
        movie = Movie.objects.create(
            title=movie_title,
            description=movie_description,
        )

        if genres_ids:
            movie.genres.set(genres_ids)

        if actors_ids:
            movie.actors.set(actors_ids)

    return movie
