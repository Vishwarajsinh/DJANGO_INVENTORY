# Generated by Django 2.2.15 on 2020-10-09 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issueorderitem',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='ItemDetails',
        ),
    ]