from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CandidateSerializer
from django.http import HttpResponse
from .models import Candidate

@api_view(['GET', 'PATCH'])
def candidate_list(request):
    """
    List all code candidates, or create a new snippet.
    """
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        qs = Candidate.objects.filter(name=request.data['name']).first()  # Already unique so adding first() is okay
        serializer = CandidateSerializer(qs, data=request.data, partial=True)
        if serializer.is_valid() and qs:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    candidates_data = Candidate.objects.all()
    for person in candidates_data:
        print("Name of candidate is ", person.name)
    return HttpResponse("This url is working")
