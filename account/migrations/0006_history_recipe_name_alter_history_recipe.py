# Generated by Django 4.0.2 on 2022-04-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='recipe_name',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='recipe',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
