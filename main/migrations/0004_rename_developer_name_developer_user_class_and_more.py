# Generated by Django 4.2.5 on 2023-11-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_developer_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='developer_name',
            new_name='user_class',
        ),
        migrations.AddField(
            model_name='developer',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
    ]