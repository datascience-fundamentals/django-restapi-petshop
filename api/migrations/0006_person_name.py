# Generated by Django 5.1.4 on 2024-12-17 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_person_age_alter_person_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default='admin', max_length=50),
            preserve_default=False,
        ),
    ]
