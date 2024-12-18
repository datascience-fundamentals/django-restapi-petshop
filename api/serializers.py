from rest_framework import serializers
from . import models


class PersonSerializer(serializers.ModelSerializer):
    dni = serializers.CharField(min_length=8, max_length=8, required=True)
    gender = serializers.ChoiceField(choices=["0", "1"], required=True)
    age = serializers.IntegerField(min_value=0, max_value=100, required=True)

    class Meta:
        model = models.Person
        fields = ["id", "name", "dni", "gender", "age"]
        read_only_fields = ["id"]

    def validate_dni(self, value: str):
        if not value.isdigit():
            raise serializers.ValidationError("DNI must be numeric")
        return value
