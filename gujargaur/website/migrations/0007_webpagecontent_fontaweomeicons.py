# Generated by Django 3.2 on 2021-05-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_webpagecontent_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpagecontent',
            name='fontaweomeicons',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
