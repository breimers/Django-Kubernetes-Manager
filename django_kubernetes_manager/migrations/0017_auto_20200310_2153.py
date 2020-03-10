# Generated by Django 3.0.4 on 2020-03-10 21:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('django_kubernetes_manager', '0016_auto_20200310_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kubernetesdeployment',
            name='kind',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='kubernetesingress',
            name='kind',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='kubernetesjob',
            name='kind',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='kubernetesservice',
            name='kind',
            field=models.CharField(max_length=16),
        ),
        migrations.CreateModel(
            name='KubernetesNamespace',
            fields=[
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', verbose_name='slug')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('deployed', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('labels', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('annotations', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True)),
                ('api_version', models.CharField(default='v1', max_length=16)),
                ('kind', models.CharField(max_length=16)),
                ('exists', models.BooleanField(default=False)),
                ('cluster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_kubernetes_manager.TargetCluster')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
