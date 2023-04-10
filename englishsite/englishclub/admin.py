from django.contrib import admin
from .models import *
# Register your models here.







@admin.register(VocabularyModel)
class BlogAdmin(admin.ModelAdmin):
    autocomplete_fields = ['userid']
    list_display = ['en','ru']

    def get_form(self, request, obj=None, change=False, **kwargs):
        form=super(BlogAdmin,self).get_form(request,obj,**kwargs)
        form.base_fields['userid'].initial=request.user
        if str(request.user)!='fedor':
            form.base_fields['userid'].disabled=request.user

        return form



class NewFileAdmin(admin.ModelAdmin):
    exclude = ('user_id',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.userid = request.user
        super().save_model(request, obj, form, change)