from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    # kind = serializers.CharField()
    kind = serializers.ChoiceField(
        choices=Category.CategoryKindChoices.choices,
    )    
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)