# Generated by Django 3.1.1 on 2020-09-21 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='visible',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
