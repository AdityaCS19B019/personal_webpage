# Generated by Django 4.0.5 on 2022-07-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('Org', models.CharField(max_length=50)),
            ],
        ),
    ]