# Generated by Django 2.1.7 on 2019-05-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20190515_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mix',
            name='mix_title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='alcohol_percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Mix',
        ),
    ]
