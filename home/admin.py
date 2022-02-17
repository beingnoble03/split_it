from django.contrib import admin
from home.models import *

# Register your models here.

admin.site.register(Transaction)
admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Purchase)
admin.site.register(ProfilePicture)