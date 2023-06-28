# Generated by Django 4.2.2 on 2023-06-27 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='class_group_student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher', to='website.class'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='full_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Class', to='website.school'),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='website.class'),
        ),
    ]