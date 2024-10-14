from django.contrib import admin
from django import forms
# Register your models here.
from .models import Snippet

class SnippetAdminForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields  = '__all__'
        help_text = {
            'code': 'Enter your code here',
        }
        fieldsets = (
        (None, {
            'fields':('title', 'language')
        }),
        ('Content',{
            'fields':('code',),
            'description': 'Selection for the code snippet itself.'
        }),
        )
@admin.register(Snippet)
# “ to display more fields in the list view and add a search bar 
class SnippetAdmin(admin.ModelAdmin):
    form  = SnippetAdminForm
    # list_display = ('title', 'language', 'created_at')
    # list_filter = ('language',)
    # search_field = ('title', 'code')
