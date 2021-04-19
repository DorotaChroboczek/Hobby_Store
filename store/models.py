from django.db.models import *

from accounts.models import Profile


class Overcategory(Model):
    class Meta:
        verbose_name = 'Overcategory'
        verbose_name_plural = 'Overcategories'

    name = CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def categories(self):
        categories = self.category_set.all()
        return categories


class Category(Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=50)
    overcategory = ForeignKey(Overcategory, on_delete=CASCADE)
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

    @property
    def imageURL(self):
        if self.image:
            url = self.image.url
        else:
            url = ''
        return url


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

    @property
    def category(self):
        return self.subcategory.category

    @property
    def overcategory(self):
        return self.subcategory.category.overcategory

    @property
    def imageURL(self):
        if self.image:
            url = self.image.url
        else:
            url = ''
        return url


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

    @property
    def name(self):
        return self.meta_product.name

    @property
    def imageURL(self):
        image = self.meta_product.image
        if image:
            url = self.meta_product.image.url
        else:
            url = ''
        return url


class ProductPromotion(Model):
    product = OneToOneField(Product, on_delete=CASCADE)
    price = DecimalField(max_digits=6, decimal_places=2)

    @property
    def name(self):
        return self.product.meta_product

    @property
    def measure(self):
        return self.product.measure

    @property
    def package(self):
        return self.product.package

    @property
    def standard_price(self):
        return self.product.price

    @property
    def percentage_of_the_promotion(self):
        value_in_percents = round((self.product.price / self.price) * 10)
        return value_in_percents


class Order(Model):
    customer = ForeignKey(Profile, on_delete=SET_NULL, null=True, blank=True)
    date_ordered = DateTimeField(auto_now_add=True)
    complete = BooleanField(default=False, null=True, blank=True)
    transaction_id = CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def order_items(self):
        order_items = self.orderitem_set.all()
        return order_items

    @property
    def cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.total for item in order_items])
        return total

    @property
    def cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


class OrderItem(Model):
    product = ForeignKey(Product, on_delete=SET_NULL, null=True, blank=True)
    order = ForeignKey(Order, on_delete=SET_NULL, null=True, blank=True)
    quantity = IntegerField(default=0, null=True, blank=True)
    date_added = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.meta_product.name

    @property
    def total(self):
        total = self.product.price * self.quantity
        return total
