# Generated by Django 4.1.3 on 2023-02-22 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_staff_alter_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stock_code_1',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='stock_code_1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='stock_code_2',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='stock_code_2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='stock_code_3',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='stock_code_3'),
        ),
    ]