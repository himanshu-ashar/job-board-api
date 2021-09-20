from rest_framework.generics import get_object_or_404
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from jobboard.models import JobOffer
from jobboard.api.serializers import JobOfferSerializer

class JobOfferListCreateAPIView(APIView):

    def get(self, request):
        jobs = JobOffer.objects.filter(available=True)
        serializer = JobOfferSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobOfferDetailAPIView(APIView):

    def get_object(self, id):
        job = get_object_or_404(JobOffer, id=id)
        return job

    def get(self, request, id):
        job = self.get_object(id)
        serializer = JobOfferSerializer(job)
        return Response(serializer.data)

    def put(self, request, id):
        job = self.get_object(id)
        serializer = JobOfferSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        job = self.get_object(id)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)