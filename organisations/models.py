from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    
    # Represents the time of day selections possible for
    # an event.
    
    
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
        # Represents whether the event is being held
        # digitally or physically.

        ("Online", "Online"),
        ("Offline", "Offline")
    ]

    POSTCODE_CHOICES = [
        # This is a selector for Birmingham postcodes,
        # designed to restrict selections for Birmingham
        # only. There are more elegant ways of achieving this
        # however this is the MVP form. Any omitted postcode
        # startpoints are intentional - eg, B22 does not exist,
        # and a number of postcodes do not lie within anyone's
        # conception of Birmingham.
        ("B1", "B1"),
        ("B2", "B2"),
        ("B3", "B3"),
        ("B4", "B4"),
        ("B5", "B5"),
        ("B6", "B6"),
        ("B7", "B7"),
        ("B8", "B8"),
        ("B9", "B9"),
        ("B10", "B10"),
        ("B11", "B11"),
        ("B12", "B12"),
        ("B13", "B13"),
        ("B14", "B14"),
        ("B15", "B15"),
        ("B16", "B16"),
        ("B17", "B17"),
        ("B18", "B18"),
        ("B19", "B19"),
        ("B20", "B20"),
        ("B21", "B21"),
        ("B23", "B23"),
        ("B24", "B24"),
        ("B25", "B25"),
        ("B26", "B26"),
        ("B27", "B27"),
        ("B28", "B28"),
        ("B29", "B29"),
        ("B30", "B30"),
        ("B31", "B31"),
        ("B32", "B32"),
        ("B33", "B33"),
        ("B34", "B34"),
        ("B35", "B35"),
        ("B36", "B36"),
        ("B37", "B37"),
        ("B38", "B38"),
        ("B40", "B40"),
        ("B42", "B42"),
        ("B43", "B43"),
        ("B44", "B44"),
        ("B45", "B45"),
        ("B62", "B62"),
        ("B63", "B63"),
        ("B64", "B64"),
        ("B65", "B65"),
        ("B66", "B66"),
        ("B67", "B67"),
        ("B68", "B68"),
        ("B69", "B69"),
        ("B70", "B70"),
        ("B71", "B71"),
        ("B72", "B72"),
        ("B73", "B73"),
        ("B74", "B74"),
        ("B75", "B75"),
        ("B76", "B76"),
        ("B90", "B90"),
        ("B91", "B91"),
        ("B92", "B92"),
        ("B93", "B93"),
        ("B94", "B94"),
        ("B96", "B96"),
        ("B97", "B97"),
        ("B98", "B98"),
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
    Postcode_1 = models.TextField(
        max_length=3,
        choices=POSTCODE_CHOICES,
        help_text="The postcode district selector of your event address",
        default="0"
    )
    Postcode_2 = models.TextField(
        max_length=8,
        default="1BB",
        help_text="The rest of the postcode for of your event address"
    )
    Online = models.CharField(
        max_length=7,
        choices=ONLINEOFFILINE_CHOICE,
        default="Offline",
        help_text="Whether your event is online or offline"
    )
    EventDate = models.DateTimeField(
        help_text="What date is your event being held?"
    )
    EventDescription = models.CharField(
        max_length=400,
        default="What will you be doing at this event?"
    )
