# Generated by Django 2.0.1 on 2018-01-31 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20180131_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
