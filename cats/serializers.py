# Added this file.
from rest_framework import serializers
from cats.models import Cat

class CatSerializer(serializers.ModelSerializer):

    gender = serializers.ChoiceField(choices = Cat.GENDER_CHOICES)

    class Meta:

        model = Cat

        fields = (
            'id',
            'name',
            'photo',
            'gender',
            'age',
            'weight',
            'date_admitted_to_shelter',
            'is_spayed_or_neutered',
            'physical_description',
            'about_me',
            'is_adopted'
        )