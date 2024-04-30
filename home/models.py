from django.db import models

class QRCodeData(models.Model):
    product_id = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    manufacturing_date = models.DateField()
    prize = models.IntegerField(max_length=10)

    def __str__(self):
        return self.product_name  # Or any other field you want to use for representation
