from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    @property
    def movies_count(self):
        count = self.movies.count()
        return count

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    duration = models.DurationField(null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True)
    genres = models.ManyToManyField(Genre, blank=True)

    @property
    def rating(self):
        stars_list = [review.stars for review in self.reviews.all()]
        if not stars_list:
            return 0
        average_mark = round(sum(stars_list) / len(stars_list), 2)
        return average_mark
    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)], null=True)

    def __str__(self):
        return self.text