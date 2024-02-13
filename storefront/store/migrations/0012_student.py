# Generated by Django 5.0.1 on 2024-02-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
