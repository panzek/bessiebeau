# Generated by Django 4.1.5 on 2023-02-01 15:56

from django.db import migrations, models


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
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]