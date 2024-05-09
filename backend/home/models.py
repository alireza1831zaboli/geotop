from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    national_code = models.CharField(
        max_length=10,
        validators=[RegexValidator(r"^[0-9]{10}$", "Enter a 10-digit number.")],
    )

    class Expert(models.TextChoices):
        EXPERT1 = "ali asadi"
        EXPERT2 = "reza rahimi"
        EXPERT3 = "amir kashefi"

    expert = models.CharField(max_length=100, choices=Expert.choices)

    def __str__(self):
        return self.name
