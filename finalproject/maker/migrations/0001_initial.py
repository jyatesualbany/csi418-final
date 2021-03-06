# Generated by Django 2.1.7 on 2019-03-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceQuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('answer', models.IntegerField()),
                ('choice_1', models.CharField(max_length=256)),
                ('choice_2', models.CharField(max_length=256)),
                ('choice_3', models.CharField(max_length=256)),
                ('choice_4', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
