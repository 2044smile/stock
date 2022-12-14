# Generated by Django 4.1.3 on 2022-12-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_channel_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('site_name', models.CharField(max_length=16)),
                ('url', models.URLField(max_length=255)),
                ('date', models.DateTimeField()),
                ('channel', models.ForeignKey(db_column='channel_id', on_delete=django.db.models.deletion.CASCADE, related_name='channel', to='stock.channel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
