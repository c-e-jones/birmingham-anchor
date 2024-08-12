from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    """
    Represents the time of day selections possible for
    an event.
    """
    
    TIMEOFDAY_CHOICES = [
        ("06:00", "6AM"),
        ("07:00", "7AM"),
        ("08:00", "8AM"),
        ("09:00", "9AM"),
        ("10:00", "10AM"),
        ("11:00", "11AM"),
        ("12:00", "12PM"),
        ("13:00", "1PM"),
        ("14:00", "2PM"),
        ("15:00", "3PM"),
        ("16:00", "4PM"),
        ("17:00", "5PM"),
        ("18:00", "6PM"),
        ("19:00", "7PM"),
        ("20:00", "8PM"),
        ("21:00", "9PM"),
        ("22:00", "10PM"),
        ("23:00", "11PM"),
        ("24:00", "12AM"),
        ("01:00", "1AM"),
        ("02:00", "2AM"),
        ("03:00", "3AM"),
        ("04:00", "4AM"),
        ("05:00", "5AM"),
    ]

    ONLINEOFFILINE_CHOICE = [
        """
        Represents whether the event is being held
        digitally or physically.
        """
        ("Online", "Online"),
        ("Offline", "Offline")
    ]


    EventName = models.TextField(
        max_length=200,
        help_text="The name of your event"
    )
    AddressLine1 = models.TextField(
        max_length=150,
        help_text="The first line of your event address, including street number"
    )
    AddressLine2 = models.TextField(
        max_length=150,
        help_text="The second line of your event address"
    )
    Postcode = models.TextField(
        max_length=8,
        help_text="The postcode of your event address"
    )
    Online = models.CharField(
        max_length=2,
        choices=ONLINEOFFLINE_CHOICE,
        default="Offline",
        help_text="Whether your event is online or offline"
    )
    EventDate = models.DateTimeField(
        help_text="What date is your event being held?"
    )
    EventTime = models.CharField(
        max_length=24,
        choices=TIMEOFDAY_CHOICES,
        default=0
    )
    EventDescription = models.CharField(
        max_length=400,
        default="What will you be doing at this event?"
    )
