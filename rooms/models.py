from django.db import models
from common.models import CommonModel


# class Room(models.Model):
class Room(CommonModel):

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHRED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(
        max_length=180,
        default="",
    )

    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price = models.PositiveBigIntegerField()
    rooms = models.PositiveBigIntegerField()

    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)

    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE
    )

    amenities = models.ManyToManyField("rooms.Amenity")

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self) -> str:
        return self.name


# class Amenity(models.Model):
class Amenity(CommonModel):
    """ Amenity Definition """
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default="", null=True)

    def __str__(self):
        return '%s: %s' % (self.name, self.description)

    class Meta:
        verbose_name_plural = "Amenities"
