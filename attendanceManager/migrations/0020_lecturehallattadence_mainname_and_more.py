# Generated by Django 5.0 on 2023-12-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0019_alter_lecturehallattadence_options'),
        ('auth_api', '0005_alter_student_name_alter_student_registernumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturehallattadence',
            name='mainName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lecturehallattadence',
            name='name',
            field=models.ManyToManyField(to='auth_api.student'),
        ),
    ]