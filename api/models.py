from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.


class CharFieldCustom(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = kwargs.get("max_length", 10)
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return f"CHAR({self.max_length})"


class Petshop(models.Model):
    # It's not necesary to specify id column, since It's create by default
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Breed(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    dni = CharFieldCustom(max_length=8)
    gender = CharFieldCustom(max_length=1)
    age = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(age__lte=100) & models.Q(age__gte=0),
                name="chk_person_age",
            ),
            models.CheckConstraint(
                check=models.Q(gender="0") | models.Q(gender="1"),
                name="chk_person_gender",
            )
        ]

    def __str__(self):
        return f"{self.dni}-{self.gender}-{self.age}"


class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    pet_id = models.IntegerField()
    petshop = models.ForeignKey(
        Petshop, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=50)
    breed = models.ForeignKey(
        Breed, on_delete=models.CASCADE, related_name="pets")
    entry_date_petshop = models.DateTimeField(auto_now_add=True)
    # blank=True -> makes the field optional in django forms and serializers
    exit_date_petshop = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            # composite key equivalent
            models.UniqueConstraint(
                fields=["pet_id", "petshop"], name="unq_pet_id_petshop")
        ]

    def __str__(self):
        return self.name


class Adoption(models.Model):
    id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="adoptions")
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="adoptions")
    adoption_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["pet", "person"], name="unq_pet_person")
        ]

    def __str__(self):
        return f"{self.pet.name}-{self.pet.petshop.name}-{self.person.name}"
