from django.db import models


from shop.models import Order

class MyStat(Order):
    class Meta:
        proxy = True