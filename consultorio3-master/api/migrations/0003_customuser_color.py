# Generated by Django 5.0.6 on 2024-08-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_role_remove_customuser_roles_customuser_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
