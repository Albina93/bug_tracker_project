from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'bio',
                    
                ),
            },
        ),
    )

admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.TicketModel)