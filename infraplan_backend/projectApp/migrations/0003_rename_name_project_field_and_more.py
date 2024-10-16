# Generated by Django 5.0.7 on 2024-10-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_project_assigned_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='field',
        ),
        migrations.RemoveField(
            model_name='project',
            name='assigned_users',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('un_planned', 'Un Planned'), ('planned', 'Planned'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='un_planned', max_length=20),
        ),
    ]
