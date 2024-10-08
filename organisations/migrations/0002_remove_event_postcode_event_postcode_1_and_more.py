# Generated by Django 4.2.14 on 2024-08-12 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='Postcode',
        ),
        migrations.AddField(
            model_name='event',
            name='Postcode_1',
            field=models.TextField(choices=[('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('B8', 'B8'), ('B9', 'B9'), ('B10', 'B10'), ('B11', 'B11'), ('B12', 'B12'), ('B13', 'B13'), ('B14', 'B14'), ('B15', 'B15'), ('B16', 'B16'), ('B17', 'B17'), ('B18', 'B18'), ('B19', 'B19'), ('B20', 'B20'), ('B21', 'B21'), ('B23', 'B23'), ('B24', 'B24'), ('B25', 'B25'), ('B26', 'B26'), ('B27', 'B27'), ('B28', 'B28'), ('B29', 'B29'), ('B30', 'B30'), ('B31', 'B31'), ('B32', 'B32'), ('B33', 'B33'), ('B34', 'B34'), ('B35', 'B35'), ('B36', 'B36'), ('B37', 'B37'), ('B38', 'B38'), ('B40', 'B40'), ('B42', 'B42'), ('B43', 'B43'), ('B44', 'B44'), ('B45', 'B45'), ('B62', 'B62'), ('B63', 'B63'), ('B64', 'B64'), ('B65', 'B65'), ('B66', 'B66'), ('B67', 'B67'), ('B68', 'B68'), ('B69', 'B69'), ('B70', 'B70'), ('B71', 'B71'), ('B72', 'B72'), ('B73', 'B73'), ('B74', 'B74'), ('B75', 'B75'), ('B76', 'B76'), ('B90', 'B90'), ('B91', 'B91'), ('B92', 'B92'), ('B93', 'B93'), ('B94', 'B94'), ('B96', 'B96'), ('B97', 'B97'), ('B98', 'B98')], default='0', help_text='The postcode district selector of your event address', max_length=3),
        ),
        migrations.AddField(
            model_name='event',
            name='Postcode_2',
            field=models.TextField(default='1BB', help_text='The rest of the postcode for of your event address', max_length=8),
        ),
        migrations.AlterField(
            model_name='event',
            name='EventTime',
            field=models.CharField(choices=[('06:00', '6AM'), ('07:00', '7AM'), ('08:00', '8AM'), ('09:00', '9AM'), ('10:00', '10AM'), ('11:00', '11AM'), ('12:00', '12PM'), ('13:00', '1PM'), ('14:00', '2PM'), ('15:00', '3PM'), ('16:00', '4PM'), ('17:00', '5PM'), ('18:00', '6PM'), ('19:00', '7PM'), ('20:00', '8PM'), ('21:00', '9PM'), ('22:00', '10PM'), ('23:00', '11PM'), ('24:00', '12AM'), ('01:00', '1AM'), ('02:00', '2AM'), ('03:00', '3AM'), ('04:00', '4AM'), ('05:00', '5AM')], default=0, help_text='What time of day is your event being held?', max_length=24),
        ),
    ]
