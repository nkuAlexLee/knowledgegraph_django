# Generated by Django 4.2 on 2023-07-17 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agriculture_knowledgegraph_django_model', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sys_email_code',
            old_name='EXPIRE',
            new_name='SEND_TIMESTAMP',
        ),
        migrations.AddField(
            model_name='sys_email_code',
            name='MSG',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
