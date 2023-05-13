from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import (
    Director,
    Movie,
    Review,
    Genre
                     )

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = 'title rating reviews'.split()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)
    movie_id = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(required=True)


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

class GenresValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

class MovieValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    duration = serializers.DurationField()
    director_id = serializers.IntegerField(min_value=1)
    genres = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError("Director doesn't exists")
        return director_id

    def validate_genres(self, genres):
        genres_db = Genre.objects.filter(id__in=genres)
        if len(genres_db) != len(genres):
            genres_db_ids = set(genre.id for genre in genres_db)
            diff_values = [genre_id for genre_id in genres if genre_id not in genres_db_ids]
            raise ValidationError(f"Genres doesn't exists: {diff_values}")
        return genres