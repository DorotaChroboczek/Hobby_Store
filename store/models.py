from django.db.models import *


class Category(Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=50)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
