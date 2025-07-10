from django.contrib import admin

from topco_automations.models import MailAutomation

# Register your models here.


admin.site.register(
    [
        MailAutomation,
    ]
)
