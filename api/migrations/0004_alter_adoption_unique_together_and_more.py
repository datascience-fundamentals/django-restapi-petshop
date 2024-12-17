# Generated by Django 5.1.4 on 2024-12-17 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pet_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='adoption',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='adoption',
            constraint=models.UniqueConstraint(fields=('pet', 'person'), name='unq_pet_person'),
        ),
        migrations.AddConstraint(
            model_name='person',
            constraint=models.CheckConstraint(condition=models.Q(('age__lte', 100), ('age__gte', 0)), name='chk_person_age'),
        ),
        migrations.AddConstraint(
            model_name='pet',
            constraint=models.UniqueConstraint(fields=('pet_id', 'petshop'), name='unq_pet_id_petshop'),
        ),
    ]