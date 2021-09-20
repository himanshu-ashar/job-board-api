from django.urls import path
from jobboard.api.views import JobOfferDetailAPIView, JobOfferListCreateAPIView

urlpatterns = [
    path("jobs/", JobOfferListCreateAPIView.as_view(), name="job-list"),
    path("jobs/<int:id>/", JobOfferDetailAPIView.as_view(), name="job-detail")
]