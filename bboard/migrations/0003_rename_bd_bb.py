# Generated by Django 4.2.2 on 2023-06-30 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bd_options_alter_bd_content_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bd',
            new_name='Bb',
        ),
    ]
