# Generated by Django 4.1.3 on 2022-11-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarnMgt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=9999)),
                ('Quantity', models.IntegerField(max_length=9999)),
                ('Price', models.IntegerField(max_length=9999)),
            ],
        ),
    ]
