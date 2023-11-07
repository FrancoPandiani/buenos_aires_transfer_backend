# Generated by Django 3.2.16 on 2023-11-07 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('budget', models.CharField(blank=True, max_length=100)),
                ('contact_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]