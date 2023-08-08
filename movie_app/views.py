from rest_framework.response import Response
from rest_framework import status
from .models import (
    Director,
    Movie,
    Review,
    Genre
)
from .serializers import (
    DirectorSerializer,
    DirectorValidateSerializer,
    MovieSerializer,
    MovieValidateSerializer,
    ReviewSerializer,
    ReviewValidateSerializer,
    MovieReviewSerializer,
    GenreSerializer,
    GenresValidateSerializer
                          )
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.pagination import PageNumberPagination


class GenreListAPIView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = GenresValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        genre = Genre.objects.create(name=name)
        return Response(data=GenreSerializer(genre).data)

class GenreDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            item = Genre.objects.get(id=id)
        except Genre.DoesNotExist:
            return Response(data={'error': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = GenresValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.name = serializer.is_valid.get('name')
        item.save()
        return Response(data=GenreSerializer(item).data)

class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.is_valid.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data)

class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            item = Director.objects.get(id=id)
        except Director.DoesNotExist:
            return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.name = serializer.is_valid.get('name')
        item.save()
        return Response(data=DirectorSerializer(item).data)

class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        # duration = timedelta(hours=int(duration_str.split(":")[0]), minutes=int(duration_str.split(":")[1]), seconds=int(duration_str.split(":")[2]))
        director_id = serializer.validated_data.get('director_id')
        genres = serializer.validated_data.get('genres')
        movie = Movie.objects.create(title=name, description=description, duration=duration, director_id=director_id)
        movie.genres.set(genres)
        return Response(data=MovieSerializer(movie).data)

class MovieReviewAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer
    pagination_class = PageNumberPagination

class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            item = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response(data={'error': 'Director not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.title = serializer.validated_data.get('name')
        item.description = serializer.validated_data.get('description')
        # duration_str = request.data.get('duration')
        # duration_time = timedelta(hours=int(duration_str.split(":")[0]), minutes=int(duration_str.split(":")[1]), seconds=int(duration_str.split(":")[2]))
        item.duration = serializer.validated_data.get('duration')
        item.director_id = serializer.validated_data.get('director_id')
        item.save()
        return Response(data=MovieSerializer(item).data)

class ReviewListApIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.is_valid.get('text')
        movie_id = serializer.is_valid.get('movie_id')
        stars = serializer.is_valid.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        return Response(data=ReviewSerializer(review).data)

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        try:
            item = Review.objects.get(id=kwargs['id'])
        except Review.DoesNotExist:
            return Response(data={'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)


        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item.text = serializer.is_valid.get('text')
        item.movie_id = serializer.is_valid.get('movie_id')
        item.stars = serializer.is_valid.get('stars')
        item.save()
        return Response(data=ReviewSerializer(item).data)