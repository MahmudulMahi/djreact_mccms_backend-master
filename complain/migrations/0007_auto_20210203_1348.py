# Generated by Django 3.1.1 on 2021-02-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0006_complain_table_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain_table',
            name='image_field',
            field=models.FileField(default='files/logo512.png', upload_to='files/'),
        ),
    ]