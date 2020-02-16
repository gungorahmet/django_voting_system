from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CandidateSerializer, CandidateVoteSerializer
from django.http import HttpResponse
from .models import Candidate

@api_view(['GET', 'PATCH'])
def candidate_list(request):
    """
    List all code candidates
    """
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        DATA = request.data
        qs = Candidate.objects.filter(name=DATA['name']).first()  # Already unique so adding first() is okay
        # TODO try except should be added
        qs.vote_count = qs.vote_count + 1
        serializer = CandidateVoteSerializer(qs, data=DATA, partial=True)
        if serializer.is_valid() and qs:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    candidates_data = Candidate.objects.all()
    for person in candidates_data:
        print("Name of candidate is ", person.name)
    return HttpResponse("This url is working")
