from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    programmable_call = models.BooleanField(default=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'