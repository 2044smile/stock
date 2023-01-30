# Generated by Django 4.1.3 on 2023-01-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_channel_options_alter_stock_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresidentBriefing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PresidentFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'PresidentFact',
                'verbose_name_plural': 'PresidentFacts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['-created_at'], 'verbose_name': 'Stock', 'verbose_name_plural': 'Stocks'},
        ),
    ]