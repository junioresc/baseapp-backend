# Generated by Django 5.0.4 on 2024-04-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp_url_shortening", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shorturl",
            name="full_url",
            field=models.URLField(max_length=2000),
        ),
    ]