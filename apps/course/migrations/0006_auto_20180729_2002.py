# Generated by Django 2.0.5 on 2018-07-29 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_courseorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorder',
            name='expire_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='courseorder',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='course.Course'),
        ),
    ]