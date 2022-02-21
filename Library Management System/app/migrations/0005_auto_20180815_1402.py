# Generated by Django 2.1 on 2018-08-15 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180815_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='rbook',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rbook',
            name='issue_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.Issue'),
            preserve_default=False,
        ),
    ]