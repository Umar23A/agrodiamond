from django.db import models
from agro.mixins import TranslateMixin
from django.utils.translation import gettext_lazy as _
import os
from datetime import datetime
import random
from django.contrib.auth.models import User

def upload_to(name):
    def handle(instance, filename):
        ext = os.path.splitext(filename)[1]

        return "{}/{:%Y}/{:%m}/{:%Y-%m-%d-%H-%M-%S}-{}{}".format(
            name,
            datetime.now(),
            datetime.now(),
            datetime.now(),
            random.randint(100000, 999999),
            ext
        )
    return handle


class Category(TranslateMixin,models.Model):
    translate_attributes = ['name']
    name_uz = models.CharField(max_length=50,verbose_name=_("Nomi (uz)"))
    name_en = models.CharField(max_length=50, verbose_name=_("Nomi (en)"))
    file = models.FileField(upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Post(TranslateMixin,models.Model):
    translate_attributes = ['nomi', 'content']

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nomi_uz = models.CharField(max_length=50,verbose_name=_("Nomi (uz)"))
    nomi_en = models.CharField(max_length=50,verbose_name=_("Nomi (en)"))
    content_uz = models.CharField(max_length=500, verbose_name=_("Content (uz)"), null=True, blank=True)
    content_en = models.CharField(max_length=500, verbose_name=_("Content (en)"), null=True, blank=True)
    image = models.FileField(upload_to='media')

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Tovar nomi'
        verbose_name_plural = 'Tovar nomlari'


class Service(TranslateMixin, models.Model):
    translate_attributes = ['subject', 'content']
    video = models.FileField(upload_to='video/')
    subject_uz = models.CharField(max_length=50, verbose_name=_("Subject (uz)"), null=True, blank=True)
    subject_en = models.CharField(max_length=50, verbose_name=_("Subject (en)"), null=True, blank=True)
    content_uz = models.CharField(max_length=10000, verbose_name=_("Content (uz)"), null=True, blank=True)
    content_en = models.CharField(max_length=10000, verbose_name=_("Content (en)"), null=True, blank=True)

    def __str__(self):
        return self.subject_uz

    class Meta:
        verbose_name = 'Servis nomi'
        verbose_name_plural = 'Servis nomlari'