# Generated by Django 3.1.1 on 2021-01-28 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0005_auto_20210128_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain_table',
            name='status',
            field=models.CharField(default='pending request', max_length=50),
        ),
    ]