# Generated by Django 2.0.5 on 2018-07-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_desc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.URLField(null=True),
        ),
    ]