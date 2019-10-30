# Generated by Django 2.2.6 on 2019-10-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0015_auto_20190906_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencedataset',
            name='is_joint_dataset',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='referencedatasetfield',
            name='data_type',
            field=models.IntegerField(choices=[(1, 'Character field'), (2, 'Integer field'), (3, 'Float field'), (4, 'Date field'), (5, 'Time field'), (6, 'Datetime field'), (7, 'Boolean field'), (8, 'Linked Reference Dataset'), (9, 'Universal unique identifier field'), (10, 'Auto incrementing integer field')]),
        ),
    ]