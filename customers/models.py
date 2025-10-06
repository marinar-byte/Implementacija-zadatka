from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# from products.models import Product


class Customer(models.Model):
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=11, validators=[RegexValidator(regex=r'^\d{11}$', message='OIB mora sadrzavti tocno 11 znamenki.')])  # 
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    #items = models.ManyToManyField(Product, through='OfferItem')  # Many-to-Many relationship with Product

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Override save to include any custom logic before saving.
        Django automatically handles insert/update based on whether the instance has a primary key.
        """
        super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):
        """
        Create an Offer instance from a tuple.
        Args:
            data (tuple): A tuple containing (id, customer_id, date, sub_total, tax, total).
        Returns:
            Offer: An instance of Offer.
        """
        return cls(
            id=data[0],
            name=data[1],
            vat_id=data[2],
            street=data[3],
            city=data[4],
            country=data[5],
        )

    @classmethod
    def get_all(cls):
        """
        Retrieve all Offer instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Offer objects.
        """
        return cls.objects.all()