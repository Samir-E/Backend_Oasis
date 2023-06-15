from rest_framework import viewsets

from .conf.permissions import IsAdminUserOrReadOnly
from .serializers import PositionSerializer, SectionSerializer
from .models import Positions, Sections


# Create your views here.
# class SectionViewSet(viewsets.ModelViewSet):
#     queryset = Sections.objects.all().order_by('-id')
#     serializer_class = SectionSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.all().order_by('-id')
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUserOrReadOnly]
