# Generated by Django 5.0.4 on 2024-04-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]