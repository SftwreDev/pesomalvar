# Generated by Django 4.0.3 on 2022-07-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_merge_20220718_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='address',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
