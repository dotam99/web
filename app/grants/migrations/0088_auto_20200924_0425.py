# Generated by Django 2.2.4 on 2020-09-24 04:25

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0087_grantstat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grant',
            name='backup_clr_prediction_curve',
        ),
        migrations.AlterField(
            model_name='grantstat',
            name='grant',
            field=models.ForeignKey(help_text='Grant to add stats for this grant', on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='grants.Grant'),
        ),
        migrations.CreateModel(
            name='GrantCLRCalculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('latest', models.BooleanField(db_index=True, default=False, help_text='Is this calc the latest?')),
                ('clr_prediction_curve', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2), blank=True, default=list, help_text='5 point curve to predict CLR donations.', size=None)),
                ('grant', models.ForeignKey(help_text='The grant', on_delete=django.db.models.deletion.CASCADE, related_name='clr_calculations', to='grants.Grant')),
                ('grantclr', models.ForeignKey(help_text='The grant CLR Round', on_delete=django.db.models.deletion.CASCADE, related_name='clr_calculations', to='grants.GrantCLR')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
