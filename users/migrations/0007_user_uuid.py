# Generated by Django 4.2.4 on 2023-08-20 08:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]