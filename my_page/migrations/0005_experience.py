# Generated by Django 4.0.5 on 2022-08-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_page', '0004_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('Desg', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=20)),
                ('Desc', models.TextField()),
            ],
        ),
    ]