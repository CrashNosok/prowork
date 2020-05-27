from django.contrib import admin
from .models import Agent

# admin.site.register(Agent)

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'city', 'profession')
