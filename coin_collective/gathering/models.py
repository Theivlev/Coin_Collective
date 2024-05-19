from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

DONATION_PURPOSE = (
        ('Birthday', 'День рождения'),
        ('Wedding', 'Свадьба'),
        ('Charity', 'Благотворительность'),
    )


class Payment(models.Model):
    donator = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Пожертвователь'
        )
    amount = models.DecimalField(
        decimal_places=2, max_digits=8, verbose_name='Сумма платежа'
        )
    collect = models.ForeignKey(
        'Collect', on_delete=models.CASCADE,
        related_name='payments',
        verbose_name='Сбор'
        )
    created = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата платежа'
        )

    def __str__(self):
        return (
            f'Платеж на сумму {self.amount} руб. '
            f'поступил на сбор {self.collect}'
        )


class Collect(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='collects',
        verbose_name='Автор сбора'
        )
    gathering_name = models.CharField(
        max_length=100, verbose_name='Название сбора')
    donation_purpose = models.CharField(
        max_length=200, choices=DONATION_PURPOSE, verbose_name='Цель сбора'
        )
    description = models.TextField(verbose_name='Описание сбора')
    all_amount = models.DecimalField(
        decimal_places=2, max_digits=8, verbose_name='Запланированная сумма'
        )
    current_amount = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        blank=True,
        null=True,
        default=None,
        verbose_name='Собрано',
        )
    donators_count = models.PositiveIntegerField(
        default=0, verbose_name='Количество пожертвовавших'
        )
    cover_image = models.ImageField(
        upload_to='media/',
        blank=True,
        null=True,
        verbose_name='Обложка сбора'
        )
    end_datetime = models.DateTimeField(
        verbose_name='Дата и время завершения сбора'
        )

    def __str__(self):
        return (
            f'{self.author} создал сбор "{self.gathering_name}" '
            f'на сумму {self.all_amount}'
        )
