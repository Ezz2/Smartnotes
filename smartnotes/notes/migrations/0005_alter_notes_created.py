# Generated by Django 4.2.1 on 2023-08-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_notes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date&Time Created'),
        ),
    ]
