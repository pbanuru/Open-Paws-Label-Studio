# Generated by Django 3.2.25 on 2024-05-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20231201_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='advocacy_approach',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='user',
            name='advocacy_diplomacy',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='user',
            name='advocacy_empiricism',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='user',
            name='advocacy_focus',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='user',
            name='advocacy_intersectionality',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='user',
            name='advocacy_rights',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='user',
            name='advocate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='current_lifestyle',
            field=models.CharField(blank=True, max_length=256, verbose_name='current lifestyle'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=256, verbose_name='role'),
        ),
    ]
