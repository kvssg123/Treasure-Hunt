from django.contrib import admin

# Register your models here.
from .models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display=('id','username','email','best_time','curr_level',)
    ordering=('best_time','id')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('-best_time')

admin.site.register(Player, PlayerAdmin)

