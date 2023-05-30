from django.db import IntegrityError
from rest_framework import serializers
from votes.models import Vote

class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer to limit votes to one vote per person onto the same post.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Vote
        fields = ['id', 'created_at', 'owner', 'post']

        def create(self, validated_data):
            try:
                return super().create(validated_data)
            except IntegrityError:
                raise serializers.ValidationError({
                    'detail':'Duplicate detected'
                })