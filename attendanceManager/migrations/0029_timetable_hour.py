# Generated by Django 5.0 on 2023-12-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0028_remove_timetable_friday_remove_timetable_monday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='hour',
            field=models.CharField(max_length=30, null=True),
        ),
    ]