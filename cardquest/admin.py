from django.contrib import admin
from .models import Trainer, PokemonCard, Collection

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email', 'created_at', 'updated_at')

    search_fields = ('name', 'location', 'email')

@admin.register(PokemonCard)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'created_at', 'updated_at')
    search_fields = ('name','rarity')
    
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'card', 'created_at', 'updated_at')
    search_fields = ('trainer', 'card')
