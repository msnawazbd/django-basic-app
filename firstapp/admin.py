from django.contrib import admin
from firstapp.models import Topic, Websites, AccessRecord


admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Websites)
