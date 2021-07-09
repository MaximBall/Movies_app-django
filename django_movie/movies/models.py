from django.db import models


class Category(models.Model):
    """""CATEGORY FILMS"""
    name = models.CharField("Категория", max_length=120)
    description = models.TextField("Описание")