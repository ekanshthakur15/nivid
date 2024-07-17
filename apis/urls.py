from django.urls import path

from .views import *

urlpatterns = [
    path("services/",ServiceAPIView.as_view()),
    path('services/details/<int:id>/', ServcieDetailView.as_view()),
    path("case-studies/",CaseStudyListAPIView.as_view()),
    path("case-studies/details/<int:id>/", CaseStudyDetailAPIView.as_view()),
    path("companies/", CompanyListAPIView.as_view()),
    path("case-studies/segments/<int:id>/", SegmentsAPIView.as_view()),
    path("services/sub-services/<int:id>/", SubServiceAPIView.as_view())
]