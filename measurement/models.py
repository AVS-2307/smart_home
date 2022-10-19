from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название датчика')
    description = models.TextField(blank=True, verbose_name='Описание датчика')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Датчик создан')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Датчик обновлен')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['-created_at']


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Измерение обновлено')  # как можно
    # обойти добавление этого поля, чтобы исключить ошибку "нулевое значение в столбце нарушает ограничение not-null",
    # при этом сохранив поле sensor ниже co связью "один-ко-многим"?
    sensor = models.ForeignKey(Sensor, null=True, on_delete=models.CASCADE, related_name="measurements",
                               verbose_name='Название счетчика')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-created_at']
