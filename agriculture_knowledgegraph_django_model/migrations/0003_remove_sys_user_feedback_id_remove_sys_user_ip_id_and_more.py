# Generated by Django 4.2.3 on 2023-07-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriculture_knowledgegraph_django_model', '0002_rename_expire_sys_email_code_send_timestamp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sys_user_feedback',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sys_user_ip',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sys_user_name',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sys_user_token',
            name='id',
        ),
        migrations.AlterField(
            model_name='sys_user_feedback',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sys_user_ip',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sys_user_name',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sys_user_token',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
