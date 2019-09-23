from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    is_vege = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    dishes = models.ManyToManyField(Dish, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def dishes_number(self):
        print(self.dish_set.count())
        return self.dish_set.count()
