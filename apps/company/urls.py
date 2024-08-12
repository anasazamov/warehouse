from django.urls import path
from apps.company.views import *

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<uuid:company_id>/sales/', CompanySalesView.as_view(), name='company-sales'),
    path('companies/<uuid:uuid>/', CompanyDetailView.as_view(), name='company-update'),
]
