# Generated by Django 3.0.3 on 2020-03-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('applications', '0020_applicationtemplate_gitlab_project_id')]

    operations = [
        migrations.AddField(
            model_name='applicationinstance',
            name='commit_id',
            field=models.CharField(max_length=8, null=True),
        )
    ]
