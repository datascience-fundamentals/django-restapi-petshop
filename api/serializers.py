from rest_framework import serializers
from . import models
from datetime import datetime


"""
    serializer class -> It allows you to serialize and deserializer JSON, aplying validations
"""


class PersonModelSerializer(serializers.ModelSerializer):
    # all these properties validate the input values passed in the data property
    dni = serializers.CharField(min_length=8, max_length=8, required=True)
    gender = serializers.ChoiceField(choices=["0", "1"], required=True)
    age = serializers.IntegerField(min_value=0, max_value=100, required=True)

    class Meta:
        model = models.Person
        # fields -> define the list of properties to include in the serialized output and deserialized input
        fields = ["id", "name", "dni", "gender", "age"]
        # read_only_fields -> ensure that certain fields can not be updated by api clients
        read_only_fields = ["id"]

    # validate_<fieldname>
    def validate_dni(self, value: str):
        if not value.isdigit():
            raise serializers.ValidationError("DNI must be numeric")
        return value


class AdoptionHistSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField(
        # input_formats -> define the date format in which It will accept as valid when convert string json to date
        input_formats=["%Y-%m-%d"])
    end_date = serializers.DateTimeField(input_formats=["%Y-%m-%d"])

    def validate(self, data):
        start_date = data["start_date"]
        end_date = data["end_date"]
        if start_date > end_date:
            raise serializers.ValidationError(
                "start_date must not be greather than end_date")
        return data


class AdoptionHistModelSerializer(serializers.ModelSerializer):
    person_name = serializers.CharField(source="person.name")
    pet_name = serializers.CharField(source="pet.name")
    breed_name = serializers.CharField(source="pet.breed.name")
    adoption_date = serializers.DateTimeField(
        # format -> define the date format in which It will be deserialized
        format="%Y-%m-%d")

    class Meta:
        model = models.Adoption
        fields = ["id", "person_name", "pet_name",
                  "breed_name", "adoption_date"]
        read_only_fields = ["id"]


class BreedModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Breed
        # all fields are going to be serialize and deserialized
        fields = "__all__"
        read_only_fields = ["id"]
