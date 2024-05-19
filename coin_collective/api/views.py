from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.response import Response

from api.permissions import IsAdminOrAuthent, IsAuthorOrReadOnly
from gathering.models import Collect, Payment

from .serializers import CollectSerializer, PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAdminOrAuthent]

    def get_queryset(self):
        collect_id = self.kwargs.get('collect_id')
        payment_queryset = Payment.objects.filter(collect=collect_id)
        return payment_queryset

    def perform_create(self, serializer):
        collect_id = self.kwargs.get('collect_id')
        collect = get_object_or_404(Collect, id=collect_id)
        serializer.save(author=self.request.user, collect=collect)


class CollectViewSet(viewsets.ModelViewSet):
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @method_decorator(cache_page(60))
    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
