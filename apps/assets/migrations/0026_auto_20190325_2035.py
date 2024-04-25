# Generated by Django 2.1.7 on 2019-03-25 12:35

import assets.models.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0025_auto_20190221_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthBook',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('username', models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_@\\-\\.]*$', 'Special char not allowed')], verbose_name='Username')),
                ('_password', models.CharField(blank=True, max_length=256, null=True, verbose_name='Password')),
                ('_private_key', models.TextField(blank=True, max_length=4096, null=True, validators=[assets.models.utils.private_key_validator], verbose_name='SSH private key')),
                ('_public_key', models.TextField(blank=True, max_length=4096, verbose_name='SSH public key')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=128, null=True, verbose_name='Created by')),
                ('is_latest', models.BooleanField(default=False, verbose_name='Latest version')),
                ('version', models.IntegerField(default=1, verbose_name='Version')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset', verbose_name='Asset')),
            ],
            options={
                'verbose_name': 'AuthBook',
            },
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'ordering': ['key'], 'verbose_name': 'Node'},
        ),
    ]
