# Generated by Django 3.0.4 on 2020-04-01 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agent',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AddField(
            model_name='agent',
            name='avatar',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
