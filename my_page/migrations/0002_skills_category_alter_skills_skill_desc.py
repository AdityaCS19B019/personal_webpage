# Generated by Django 4.0.5 on 2022-07-30 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='category',
            field=models.CharField(default='Programming Language', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_desc',
            field=models.CharField(max_length=100),
        ),
    ]
