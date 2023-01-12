from rest_framework import viewsets, permissions
from .models import Lead
from .serializers import LeadSerializer

#Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):
  queryset = Lead.objects.all()
  serializer_class = LeadSerializer