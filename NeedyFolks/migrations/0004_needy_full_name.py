# Generated by Django 5.0.3 on 2024-03-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NeedyFolks', '0003_alter_needy_family_members_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='needy',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
