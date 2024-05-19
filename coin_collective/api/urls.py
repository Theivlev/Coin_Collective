from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CollectViewSet, PaymentViewSet

app_name = 'api'

router = DefaultRouter()

router.register('collects', CollectViewSet, basename='collect')
router.register(
    r'^collects/(?P<collect_id>\d+)/payments',
    PaymentViewSet,
    basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
