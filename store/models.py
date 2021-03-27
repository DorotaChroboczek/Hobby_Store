from django.db.models import *


class Category(Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=50)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        if self.image:
            url = self.image.url
        else:
            url = ''
        return url


class Subcategory(Model):
    category = ForeignKey(Category, on_delete=CASCADE)
    name = CharField(max_length=70)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class MetaProduct(Model):
    class Meta:
        verbose_name = 'Meta Product'
        verbose_name_plural = 'Meta Products'

    name = CharField(max_length=100, unique=True)
    subcategory = ForeignKey(Subcategory, on_delete=SET_NULL,
                             null=True, blank=True)
    description = TextField(max_length=800, null=False, blank=False)
    image = ImageField(null=False, blank=False)

    def __str__(self):
        return self.name


class UnitOfMeasurement(Model):
    symbol = CharField(max_length=10, unique=True)

    def __str__(self):
        return self.symbol


class Product(Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    meta_product = ForeignKey(MetaProduct, on_delete=CASCADE,
                              null=False, blank=False)
    measure = ForeignKey(UnitOfMeasurement, on_delete=CASCADE,
                         null=False, blank=False)
    package = PositiveSmallIntegerField(verbose_name='Package size',
                                        null=False, blank=False)
    price = DecimalField(max_digits=6, decimal_places=2)
    availability = IntegerField(null=False, blank=False)




