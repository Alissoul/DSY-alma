# Generated by Django 3.1.2 on 2020-11-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicicletas', '0002_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default=5678, max_length=5, unique=True),
            preserve_default=False,
        ),
    ]
