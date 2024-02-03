from django.db import models


class Category(models.Model):
    # db_index - for search acceleration and memory optimization
    name = models.CharField(max_length=250, db_index=True)

    # slug - used to get a particular category
    # explanation: https://www.w3schools.com/django/django_slug_field.php
    slug = models.SlugField(max_length=250, unique=True)

    # Django visualizes the Category class in the Admin panel as Categorys.
    # The meta configuration changes that.
    class Meta:
        verbose_name_plural = 'categories'

    # When a category is selected, the name returned from the database is generic - Category(10, Category(20
    # This changes the generic name to the name of the category
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    brand = models.CharField(max_length=250, default="un-branded")
    description = models.TextField(max_length=250)

    slug = models.SlugField(max_length=250, unique=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title
