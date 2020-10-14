# Generated by Django 3.1.2 on 2020-10-14 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20201012_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuebill',
            name='issued_by',
        ),
        migrations.AddField(
            model_name='issuebill',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.item'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issuebill',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='IssueOrderItem',
        ),
    ]
