# Generated by Django 4.0 on 2023-05-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='pic')),
                ('about', models.TextField()),
            ],
        ),
    ]
