from django.contrib import admin

from fiber.models import Cable, Panel


class InfrastructureAdmin(admin.ModelAdmin):
    list_display = ("location", "uploaded_at")

@admin.register(Cable)
class CableAdmin(InfrastructureAdmin):
    pass

@admin.register(Panel)
class PanelAdmin(InfrastructureAdmin):
    pass
