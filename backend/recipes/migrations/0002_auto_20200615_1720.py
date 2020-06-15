# Generated by Django 3.0.7 on 2020-06-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'EASY'), (2, 'INTERMEDIATE'), (3, 'HARD')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
