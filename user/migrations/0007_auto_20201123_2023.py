# Generated by Django 3.1.1 on 2020-11-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='new_create',
        ),
        migrations.RemoveField(
            model_name='service',
            name='refferd_pic',
        ),
        migrations.AddField(
            model_name='service',
            name='new_crate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='reffered_pic',
            field=models.ImageField(max_length=20, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
