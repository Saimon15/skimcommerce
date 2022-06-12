import uuid

from django.db import models

from common.models import BaseModel


class ProductCategory(BaseModel):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=256, null=False)
	description = models.CharField(max_length=500, null=True)


class Product(BaseModel):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=256, null=False)
	description = models.TextField(null=False)
	category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
	price = models.FloatField()
	primary_image = models.ImageField(upload_to='uploads/')
	secondary_image = models.ImageField(upload_to='uploads/')
	tertiary_image = models.ImageField(upload_to='uploads/')
	in_stock = models.BooleanField(default=True)
	ingredients = models.CharField(max_length=256, null=True)
	shelf_life = models.CharField(max_length=100, null=True)


