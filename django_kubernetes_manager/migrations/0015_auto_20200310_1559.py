# Generated by Django 3.0.4 on 2020-03-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_kubernetes_manager', '0014_auto_20200310_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kubernetescontainer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kubernetesdeployment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kubernetesingress',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kubernetesjob',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kubernetespodtemplate',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kubernetesservice',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kubernetesvolume',
            name='name',
        ),
        migrations.RemoveField(
            model_name='kubernetesvolumemount',
            name='name',
        ),
        migrations.AddField(
            model_name='kubernetescontainer',
            name='title',
            field=models.CharField(default='coppntainer', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kubernetesdeployment',
            name='title',
            field=models.CharField(default='deployer', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kubernetesingress',
            name='title',
            field=models.CharField(default='ing', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kubernetesjob',
            name='title',
            field=models.CharField(default='job', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kubernetespodtemplate',
            name='title',
            field=models.CharField(default='pod', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kubernetesservice',
            name='title',
            field=models.CharField(default='svc', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kubernetesvolume',
            name='title',
            field=models.CharField(default='vol', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kubernetesvolumemount',
            name='title',
            field=models.CharField(default='vmount', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kubernetescontainer',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='kubernetesdeployment',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='kubernetesingress',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='kubernetesjob',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='kubernetespodtemplate',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='kubernetesservice',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='kubernetesvolume',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='kubernetesvolumemount',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]
