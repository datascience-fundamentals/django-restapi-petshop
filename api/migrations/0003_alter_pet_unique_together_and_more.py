# Generated by Django 5.1.4 on 2024-12-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_person_gender_alter_pet_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='adoption',
            unique_together={('pet', 'person')},
        ),
        migrations.AddField(
            model_name='pet',
            name='pet_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adoption',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('pet_id', 'petshop')},
        ),
        migrations.RemoveField(
            model_name='adoption',
            name='petshop',
        ),
    ]
