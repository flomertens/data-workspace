# Generated by Django 2.2.3 on 2019-10-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0017_sourceview'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcetable',
            name='available_in_catalogue',
            field=models.BooleanField(
                default=False, help_text='Make this table available to users for download via the catalogue'),
        ),
        migrations.AddField(
            model_name='sourcetable',
            name='available_in_tools',
            field=models.BooleanField(default=True, help_text='Make this table available to users via tools'),
        ),
        migrations.AddField(
            model_name='sourceview',
            name='available_in_catalogue',
            field=models.BooleanField(
                default=True, help_text='Make this view available to users for download via the catalogue'),
        ),
    ]