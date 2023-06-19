from rest_framework import serializers
from .models import MovieOrder, Seasons
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(choices=Seasons.choices, default=Seasons.G)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        user = obj.user.email
        return user

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)



class OrderMovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)

    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()

    def get_buyed_by(self, obj):
        buyed_by = obj.user.email
        return buyed_by

    def get_title(self, obj):
        title = obj.movie.title
        return title

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)