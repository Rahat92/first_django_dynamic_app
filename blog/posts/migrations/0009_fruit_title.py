# Generated by Django 4.1 on 2022-09-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_fruit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]