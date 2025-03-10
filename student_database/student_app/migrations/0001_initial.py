# Generated by Django 5.1 on 2024-10-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', models.IntegerField(unique=True)),
                ('course', models.CharField(max_length=100)),
                ('join_date', models.DateField()),
            ],
        ),
    ]
