from django.contrib import admin
from .models import Offer, OfferItem

# Register your models here.

admin.site.register(Offer)
admin.site.register(OfferItem)