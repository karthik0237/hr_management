# Generated by Django 5.0.4 on 2024-05-06 10:09

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_city_id_alter_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.UUID('70c6afa0-59e1-4666-bb2c-97ff658e81c3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dbf12fa6-cec1-4388-a68e-1fa093ccbbc3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='educationdetails',
            name='id',
            field=models.UUIDField(default=uuid.UUID('617cec5a-6102-4b2a-a0cb-ac638a541b2a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='familymembers',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b7ad3c57-7d52-4c22-b472-cfee29ae2312'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e77f5f26-8bfc-48db-81d5-824c74021043'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='userbankdetails',
            name='id',
            field=models.UUIDField(default=uuid.UUID('e864fb21-5472-4e2c-8a21-2d8782f42414'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userexperience',
            name='id',
            field=models.UUIDField(default=uuid.UUID('be297d42-282f-49a9-b0e9-0c5088d5de76'), editable=False, primary_key=True, serialize=False),
        ),
    ]
