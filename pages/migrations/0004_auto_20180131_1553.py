# Generated by Django 2.0.1 on 2018-01-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_content_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
