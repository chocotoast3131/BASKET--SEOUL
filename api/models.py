from django.db import models

# Create your models here.
class ItemName(models.Model):
    category_name = models.TextField()
    item_code = models.CharField(max_length=3)
    kind_code = models.CharField(max_length=2)
    item_name = models.TextField()
    kind_name = models.TextField()

    def __str__(self):
        return self.item_name