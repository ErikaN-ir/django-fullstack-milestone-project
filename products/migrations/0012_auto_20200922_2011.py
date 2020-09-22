# Generated by Django 3.1.1 on 2020-09-22 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_rating_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.rating'),
        ),
    ]
