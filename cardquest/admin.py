from django.contrib import admin
from .models import Trainer, PokemonCard

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email')

    search_fields = ('name', 'location')

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity')
    search_fields = ('name',)
