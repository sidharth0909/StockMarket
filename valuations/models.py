from django.db import models

class Valuation(models.Model):
    revenue = models.FloatField()
    ebitda = models.FloatField()
    growth_rate = models.FloatField()
    current_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
