from rest_framework import serializers

from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = (
            'name',
            'vote_count'
        )

class CandidateVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['name']