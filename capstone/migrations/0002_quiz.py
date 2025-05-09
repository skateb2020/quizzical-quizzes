# Generated by Django 3.2.5 on 2022-07-30 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question1', models.TextField()),
                ('answer1', models.TextField()),
                ('question2', models.TextField()),
                ('question3', models.TextField()),
                ('answer3', models.TextField()),
                ('question4', models.TextField()),
                ('answer4', models.TextField()),
                ('question5', models.TextField()),
                ('answer5', models.TextField()),
                ('question6', models.TextField()),
                ('answer6', models.TextField()),
                ('question7', models.TextField()),
                ('answer7', models.TextField()),
                ('question8', models.TextField()),
                ('answer8', models.TextField()),
                ('question9', models.TextField()),
                ('answer9', models.TextField()),
                ('question10', models.TextField()),
                ('answer10', models.TextField()),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
