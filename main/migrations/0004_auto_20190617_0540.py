# Generated by Django 2.1.7 on 2019-06-17 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pandagulutype_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pandagulutype',
            name='pic',
        ),
        migrations.AddField(
            model_name='donateamount',
            name='pic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]