from django.db import models

class HollidayModel(models.Model):
    description = models.CharField('hollidaydescription', max_length=200)
    day = models.IntegerField('day')
    month = models.IntegerField('month')
    country = models.CharField('country', max_length=100, default=None)
    flag = models.CharField('flag_link', max_length=100, default=None)
    updated_at = models.DateTimeField(
        verbose_name='Updated At',
        auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.description
