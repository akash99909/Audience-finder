# Generated by Django 2.1.2 on 2020-12-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='devmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=10)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='form',
        ),
    ]
