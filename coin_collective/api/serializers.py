from django.core.mail import send_mail
from django.db.models import Count
from rest_framework import serializers

from gathering.models import Collect, Payment

from .service import Base64ImageField


class PaymentSerializer(serializers.ModelSerializer):
    donator = serializers.SerializerMethodField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Payment
        fields = ('id', 'donator', 'amount', 'created')

    def get_donator(self, obj):
        return {
            'donator_username': obj.donator.username,
            'amount': obj.amount,
        }

    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)
        email = payment.donator.email
        send_mail(
            'Платеж отправлен, спасибо за участие!',
            'Платеж',
            'theivlev@yandex.ru',
            [email],
            fail_silently=True,
        )
        return payment


class CollectSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    current_amount = serializers.SerializerMethodField()
    donators_count = serializers.SerializerMethodField()
    cover_image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Collect
        fields = (
            'id',
            'author',
            'gathering_name',
            'donation_purpose',
            'description',
            'all_amount',
            'current_amount',
            'cover_image',
            'donators_count',
            'end_datetime',
            )

    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"

    def create(self, validated_data):
        collect = Collect.objects.create(**validated_data)
        email = collect.author.email
        send_mail(
            'Сбор создан, только вперёд!',
            'Создание сбора',
            'theivlev@yandex.ru',
            [email],
            fail_silently=True,
        )
        return collect

    def get_current_amount(self, obj):
        current_amount = 0
        for payment in obj.payments.all():
            current_amount += payment.amount
        return current_amount

    def get_donators_count(self, obj):
        participants = obj.payments.values('donator').annotate(
            total=Count('donator')).count()
        return participants
