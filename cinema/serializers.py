from rest_framework import serializers

from cinema.models import Movie


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.info = validated_data.get("info", instance.info)
        instance.num_seats = validated_data.get(
            "num_seats",
            instance.num_seats
        )
        instance.save()
        return instance
