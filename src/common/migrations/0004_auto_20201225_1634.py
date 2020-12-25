# Generated by Django 3.1.4 on 2020-12-25 14:34

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_example_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='example',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='example',
            name='updated',
        ),
        migrations.AddField(
            model_name='example',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='example',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='publishing datetime', when={'published'}),
        ),
        migrations.AddField(
            model_name='example',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='published', max_length=100, no_check_for_status=True, verbose_name='status'),
        ),
        migrations.AddField(
            model_name='example',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed'),
        ),
        migrations.AlterField(
            model_name='example',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
    ]
