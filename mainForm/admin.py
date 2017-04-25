from django.contrib import admin
from .models import PigEntry
from .models import Flow

admin.site.register(PigEntry)
admin.site.register(Flow)