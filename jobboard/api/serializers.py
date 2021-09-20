from django.db import models
from rest_framework import serializers
from jobboard.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        fields = "__all__"