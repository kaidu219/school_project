# Generated by Django 4.2.2 on 2023-06-27 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_teacher_phone_number_teacher_pphone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='pphone_number',
            new_name='phone_number',
        ),
    ]
