# Generated by Django 2.2.4 on 2019-12-10 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0012_applicationtemplate_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationTemplateUserPermission',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                )
            ],
            options={'db_table': 'app_applicationtemplateuserpermission'},
        ),
        migrations.CreateModel(
            name='VisualisationTemplate',
            fields=[],
            options={
                'verbose_name': 'Visualisation',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('applications.applicationtemplate',),
        ),
        migrations.AddField(
            model_name='applicationtemplate',
            name='application_type',
            field=models.CharField(
                choices=[
                    (
                        'VISUALISATION',
                        'Visualisation: One instance launched and accessed by all authorized users',
                    ),
                    ('TOOL', 'Tool: A separate instance launched for each user'),
                ],
                default='TOOL',
                max_length=64,
            ),
        ),
        migrations.AddField(
            model_name='applicationtemplate',
            name='host_exact',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='applicationtemplate',
            name='user_access_type',
            field=models.CharField(
                choices=[
                    ('REQUIRES_AUTHENTICATION', 'Requires authentication'),
                    ('REQUIRES_AUTHORIZATION', 'Requires authorization'),
                ],
                default='REQUIRES_AUTHENTICATION',
                max_length=64,
            ),
        ),
        migrations.AlterField(
            model_name='applicationtemplate',
            name='host_pattern',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='applicationtemplate',
            name='spawner',
            field=models.CharField(
                choices=[('PROCESS', 'Process'), ('FARGATE', 'Fargate')],
                default='FARGATE',
                max_length=10,
            ),
        ),
        migrations.AlterUniqueTogether(
            name='applicationtemplate', unique_together={('host_exact', 'host_pattern')}
        ),
        migrations.AddIndex(
            model_name='applicationtemplate',
            index=models.Index(
                fields=['host_exact'], name='app_applica_host_ex_7bfb56_idx'
            ),
        ),
        migrations.AddField(
            model_name='applicationtemplateuserpermission',
            name='application_template',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='applications.ApplicationTemplate',
            ),
        ),
        migrations.AddField(
            model_name='applicationtemplateuserpermission',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterUniqueTogether(
            name='applicationtemplateuserpermission',
            unique_together={('user', 'application_template')},
        ),
    ]
