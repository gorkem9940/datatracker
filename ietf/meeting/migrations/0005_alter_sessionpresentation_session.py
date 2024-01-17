# Generated by Django 4.2.9 on 2024-01-12 18:31

from django.db import migrations
import django.db.models.deletion
import ietf.utils.models


class Migration(migrations.Migration):
    dependencies = [
        ("meeting", "0004_session_chat_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sessionpresentation",
            name="session",
            field=ietf.utils.models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="presentations",
                to="meeting.session",
            ),
        ),
    ]