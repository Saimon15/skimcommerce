# Generated by Django 3.2.13 on 2022-06-12 20:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('primary_image', models.ImageField(upload_to='uploads/')),
                ('secondary_image', models.ImageField(upload_to='uploads/')),
                ('tertiary_image', models.ImageField(upload_to='uploads/')),
                ('in_stock', models.BooleanField(default=True)),
                ('ingredients', models.CharField(max_length=256, null=True)),
                ('shelf_life', models.CharField(max_length=100, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
