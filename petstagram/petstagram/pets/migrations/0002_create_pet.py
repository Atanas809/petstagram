# Generated by Django 4.1.1 on 2022-10-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('personal_photo', models.URLField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
