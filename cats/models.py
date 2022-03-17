from django.db import models

class Cat(models.Model):

    # The id field is added automatically according to the Django documentation, 
    # so that is why this model does not have a primary key field specified.

    name = models.CharField(max_length = 200)
    photo = models.URLField()
    age = models.IntegerField(default = 0)
    
    FEMALE = 'F'
    MALE = 'M'

    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )

    gender = models.CharField(
        max_length = 2,
        choices = GENDER_CHOICES,
        default = FEMALE
    )

    weight = models.DecimalField(default = 0.00, max_digits = 4, decimal_places = 2)
    date_admitted_to_shelter = models.DateField()
    is_spayed_or_neutered = models.BooleanField()
    physical_description = models.TextField()
    about_me = models.TextField()
    is_adopted = models.BooleanField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name