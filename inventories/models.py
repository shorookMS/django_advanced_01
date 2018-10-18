from django.db import models
from stores.models import Store
# Create your models here.
class Inventory(models.Model):
	CHOICES = ((True,'Empty'),(False,'Not Empty'))
	name = models.CharField(max_length=255)
	store = models.ForeignKey(Store, default=1, on_delete=models.CASCADE)
	is_empty = models.BooleanField(choices = CHOICES, default = 1, blank=False)
	last_updated = models.DateTimeField(auto_now=True)
