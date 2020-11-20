# Generated by Django 3.1.2 on 2020-10-15 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0002_auto_20201007_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='recruit',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='subcategory_image',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='thumbnail_url',
            field=models.CharField(max_length=500),
        ),
    ]