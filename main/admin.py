from django.contrib import admin
from .models import Receita
from .models import Produto
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class ReceitaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Produto)
