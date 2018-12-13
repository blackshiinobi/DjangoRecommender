# Generated by Django 2.1.2 on 2018-12-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showMovies', '0004_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='movieId',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
