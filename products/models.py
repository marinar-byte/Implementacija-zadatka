from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the save method to include any custom logic.
        Django automatically handles insert/update based on whether the instance has a primary key.
        """
        super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):
        """
        Creates a Product instance from a tuple.
        Args:
            data (tuple): A tuple containing (id, name, description, price).
        Returns:
            Product: An instance of Product.
        """
        return cls(id=data[0], name=data[1], description=data[2], price=data[3])

    @classmethod
    def get_all(cls):
        """
        Retrieves all Product instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Product objects.
        """
        return cls.objects.all()
