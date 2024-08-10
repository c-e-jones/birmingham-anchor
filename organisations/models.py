from django.db import models

# Create your models here.
class Event(models.Model):
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
        ("Online", "Digial"),
        ("Offline", "Physical")
    ]


    EventName = models.TextField(max_length=200, unique=False)
    AddressLine1 = models.TextField(max_length=150, unique=False)
    AddressLine2 = models.TextField(max_length=150, unique=False)
    Postcode = models.TextField(max_length=8, unique=False)
    Online = models.CharField(max-length=2, choices=ONLINEOFFLINE_CHOICE)
    EventDate = models.DateTimeField()
    EventTime = models.CharField(max-length=24, choices=TIMEOFDAY_CHOICES)
    CreateDateAndTime = models.DateTimeField()
    EventOrganiser = models.ForeignKey()
