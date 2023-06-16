from django.db import models
from django.core.validators import MinLengthValidator
from .validators import image_size_validator_5mb, text_underscore_validator

from Petstagram.pets.models import Pet


class Photo(models.Model):
    pet_image = models.ImageField(
        blank=False,
        null=False,
        validators=(image_size_validator_5mb,),
        upload_to="photos",
    )
    # optional
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10), text_underscore_validator,),
        blank=True,
        null=True
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.pet_image}"


