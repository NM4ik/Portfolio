from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Person)
admin.site.register(Work)
admin.site.register(Skill)
admin.site.register(Technology)