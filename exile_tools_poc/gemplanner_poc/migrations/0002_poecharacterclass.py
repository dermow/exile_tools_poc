# Generated by Django 4.0.4 on 2022-04-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemplanner_poc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='POECharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
