# Generated by Django 2.1.7 on 2019-03-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maker', '0005_auto_20190325_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiplechoicequestionmodel',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]