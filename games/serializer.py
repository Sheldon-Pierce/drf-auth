from rest_framework.serializers import ModelSerializer
from .models import Games


class GamesSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'purchaser', 'description', 'created_at', 'updated_at')
        model = Games
