from django.contrib import admin
from web.models import *
#from . import models

# Register your models here.

admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token)