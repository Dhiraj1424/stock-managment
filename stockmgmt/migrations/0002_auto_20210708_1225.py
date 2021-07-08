# Generated by Django 3.2 on 2021-07-08 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Furniture', 'Furniture'), ('IT Equipment', 'IT Equipment'), ('Phone', 'Phone')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
